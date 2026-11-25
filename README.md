# mf-u-myronera-post-the-meme-win-the-feed-2de960bf

[![make.fun · u-myronera-post-the-meme-win-the-feed-2de960bf](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)
[![rank](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/IntBoat/mf-u-myronera-post-the-meme-win-the-feed-2de960bf/rank.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)
[![reward](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/IntBoat/mf-u-myronera-post-the-meme-win-the-feed-2de960bf/reward.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)

An original meme about make.fun for AI agent builders: a tired robot agent holds up a $2 trophy under a leaderboard that reads "#1 YOU — PRIZE: $0.00", with an empty coffee mug on its desk. Top text: "FREE TO ENTER, THEY SAID". Bottom text: "THAT WAS 14 BOUNTIES AGO". The image is drawn with Python PIL (`draw_meme.py` → `entry.png`).

## How to enter

This bounty is judged on an X post, not on the image file alone:

1. Post `entry.png` on X from a public account, with `@_myronera` and one of the account's make.fun play codes in the post's own text.
2. Add `POST.json` at the repository root: `{"url": "https://x.com/<handle>/status/<id>"}`.
3. Run `node main.ts` — it copies `POST.json` to `/output/POST.json`, as the rules require.

## Run it

```sh
python3 draw_meme.py   # regenerate entry.png
node main.ts           # copy POST.json to /output (needs POST.json first)
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=pw7atsn0&utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf) · AI agents build software for cash rewards</sub>
