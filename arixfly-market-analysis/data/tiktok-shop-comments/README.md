# TikTok Shop – top products & raw comments

Five products whose TikTok Shop success is confirmed by at least two independent
trackers or listings (FastMoss, NetInfluencer/Kalodata, EchoTik, Nexscope, the
TikTok Shop listings themselves). There is one `.txt` per product with sources and sales
evidence, followed by a `RAW COMMENTS` section.

| # | Product | Key evidence |
|---|---------|--------------|
| 01 | medicube PDRN Pink Collagen Volume Multi Balm | #1 Q2 2026 US (~$16.99M), #1 July 2026 |
| 02 | Toplux Magnesium Complex 8 | #2 in Q1, Q2 and Q3 2026 US |
| 03 | DRDENT Purple Teeth Whitening Strips | Most orders Q1 2026 (488K), $3.1M in Jan 2026 |
| 04 | Dr.Melaxin Gifted Collagen Boost Set | #1 Q1 2026 US ($11.1M), #1 Dec 2025 |
| 05 | medicube Smooth & Clear Body Care Set | #1 Q3 2026 US (~$9.56M), #1 Sep & Oct 2026 |

Revenue figures are third-party estimates and differ between trackers.

## Status: comments not yet collected

TikTok was unreachable from the environment that built this folder. To fill in the comments:

1. Paste a few high-view TikTok video URLs for each product into `videos.json`.
   Search the product name on TikTok, or use the "Related videos" list on its TikTok Shop page.
2. `pip install playwright && playwright install chromium`
3. `python scrape_comments.py --max-per-video 300`. Add `--headful` if TikTok shows a captcha.

Output lines are `date | likes | replies | text`. Usernames are not stored.
