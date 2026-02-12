import test from "node:test";
import assert from "node:assert/strict";

import { buildFallbackReply, classifyIntent, parseAgentEnvelope } from "../src/core/agent.mjs";

test("parseAgentEnvelope parses wrapped JSON", () => {
  const wrapped = "output:\n```json\n{\"message\":\"hi\",\"actions\":[]}\n```";
  const parsed = parseAgentEnvelope(wrapped);

  assert.equal(parsed.message, "hi");
  assert.deepEqual(parsed.actions, []);
});

test("classifyIntent identifies split request", () => {
  assert.equal(classifyIntent("split windows and create panes"), "split_layout");
});

test("fallback comparison returns table surface", () => {
  const reply = buildFallbackReply({ message: "find alternatives", mode: "assistant" });

  assert.equal(reply.surface.type, "table");
  assert.ok(reply.surface.rows.length > 0);
});
