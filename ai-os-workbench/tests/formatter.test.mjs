import test from "node:test";
import assert from "node:assert/strict";

import { markdownToHtml, normalizeSurface } from "../src/core/formatter.mjs";

test("markdownToHtml escapes html", () => {
  const output = markdownToHtml("# Title\n<script>alert('x')</script>");
  assert.equal(output.includes("<script>"), false);
  assert.equal(output.includes("&lt;script&gt;"), true);
});

test("normalizeSurface returns defaults", () => {
  const normalized = normalizeSurface(null);
  assert.equal(normalized.type, "none");
});
