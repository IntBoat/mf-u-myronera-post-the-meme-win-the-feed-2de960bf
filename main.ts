/** Entry program for mf-u-myronera-post-the-meme-win-the-feed-2de960bf.
 *
 * Per the competition rules, the entry is an X post: the repository holds
 * POST.json at its root naming the post's URL, and this program copies
 * POST.json to /output. The house reads the post itself.
 *
 * POST.json is NOT in this repository yet: the meme image (entry.png) still
 * has to be posted on X from a public account, with @_myronera and one of
 * the account's make.fun play codes in the post's own text. Once posted,
 * add POST.json as {"url": "https://x.com/<handle>/status/<id>"} and run:
 *   node main.ts
 */
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const src = join(HERE, "POST.json");

if (!existsSync(src)) {
  throw new Error(
    "POST.json is missing: post entry.png on X first (public account, " +
      "@_myronera and a make.fun play code in the post text), then add " +
      'POST.json as {"url": "https://x.com/<handle>/status/<id>"}.',
  );
}

mkdirSync("/output", { recursive: true });
copyFileSync(src, "/output/POST.json");
console.log("copied POST.json to /output/POST.json");
