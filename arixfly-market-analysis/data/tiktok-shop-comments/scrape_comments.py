"""Scrape public TikTok video comments into the per-product .txt files.

Usage:
    pip install playwright && playwright install chromium
    # add TikTok video URLs per product in videos.json, then:
    python scrape_comments.py --max-per-video 300

Opens each video page in a real browser, scrolls the comment panel, and
captures the JSON responses of TikTok's own /api/comment/list/ calls.
Only the comment text, like count, reply count and date are saved.
Usernames are not saved.

The "RAW COMMENTS" section of each product file is rewritten on every run.
"""
import argparse
import datetime as dt
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
MARKER = "RAW COMMENTS"


def scrape_video(page, url, limit):
    comments, seen = [], set()

    def on_response(resp):
        if "/api/comment/list/" not in resp.url:
            return
        try:
            data = resp.json()
        except Exception:
            return
        for c in data.get("comments") or []:
            cid = c.get("cid")
            if cid in seen:
                continue
            seen.add(cid)
            comments.append({
                "text": (c.get("text") or "").replace("\n", " ").strip(),
                "likes": c.get("digg_count", 0),
                "replies": c.get("reply_comment_total", 0),
                "date": dt.datetime.utcfromtimestamp(c.get("create_time", 0)).strftime("%Y-%m-%d"),
            })

    page.on("response", on_response)
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    # Open the comments panel if it is collapsed.
    for sel in ['[data-e2e="comment-icon"]', '[data-e2e="browse-comment-icon"]']:
        if page.locator(sel).count():
            page.locator(sel).first.click()
            break
    stale = 0
    while len(comments) < limit and stale < 8:
        before = len(comments)
        page.mouse.wheel(0, 4000)
        page.keyboard.press("End")
        page.wait_for_timeout(1500)
        stale = stale + 1 if len(comments) == before else 0
    page.remove_listener("response", on_response)
    return comments[:limit]


def write_section(path, url_blocks):
    text = path.read_text(encoding="utf-8")
    head = text.split("VIDEO URLS SCRAPED")[0]
    lines = ["VIDEO URLS SCRAPED"] + [u for u, _ in url_blocks] + ["", MARKER,
             "# format: date | likes | replies | text", ""]
    for url, comments in url_blocks:
        lines.append(f"## {url} ({len(comments)} comments)")
        for c in comments:
            lines.append(f"{c['date']} | {c['likes']} | {c['replies']} | {c['text']}")
        lines.append("")
    path.write_text(head + "\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-per-video", type=int, default=300)
    ap.add_argument("--headful", action="store_true")
    args = ap.parse_args()

    videos = json.loads((HERE / "videos.json").read_text())
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.headful)
        page = browser.new_context(locale="en-US").new_page()
        for fname, urls in videos.items():
            if not urls:
                print(f"skip {fname}: no video URLs")
                continue
            blocks = []
            for url in urls:
                got = scrape_video(page, url, args.max_per_video)
                print(f"{fname}: {len(got)} comments from {url}")
                blocks.append((url, got))
            write_section(HERE / fname, blocks)
        browser.close()


if __name__ == "__main__":
    main()
