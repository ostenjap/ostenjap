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

## Comments: collected 2026-11-23

1,840 comments from 20 videos (4 per product), pulled through Apify:

1. **Video discovery:** `xmolodtsov~tiktok-search-scraper` with 2 search terms per product (US).
   From the results, the most-commented videos whose caption or hashtags name the product were kept.
   Close variants of the products were left out (e.g. medicube's NAD+ EGF balm).
   The chosen URLs are in `videos.json`.
2. **Comments:** `clockworks~tiktok-comments-scraper`, up to 100 top-level comments per video,
   in TikTok's default order (roughly the most-liked first). Replies are not included.

| # | Product | Comments |
|---|---------|----------|
| 01 | medicube PDRN Multi Balm | 375 |
| 02 | Toplux Magnesium Complex 8 | 371 |
| 03 | DRDENT Purple Strips | 400 |
| 04 | Dr.Melaxin Gifted Collagen Boost Set | 338 |
| 05 | medicube Body Care Set | 356 |

Output lines are `date | likes | replies | text`. Usernames are not stored. Sticker- or GIF-only
comments appear as `[no text - sticker/GIF only]`. Two of the 01 videos and one of the 04 videos
compare medicube against Dr.Melaxin, so some comments there are about the competitor.

### Re-running without Apify

`scrape_comments.py` reads the same `videos.json` and writes the same format using a local browser:
`pip install playwright && playwright install chromium`, then `python scrape_comments.py --max-per-video 300`
(add `--headful` if TikTok shows a captcha). It has not been run against TikTok.
