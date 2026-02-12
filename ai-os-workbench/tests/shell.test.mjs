import test from "node:test";
import assert from "node:assert/strict";

import { isDangerousCommand, runCommand } from "../src/core/shell.mjs";

test("isDangerousCommand blocks destructive patterns", () => {
  assert.equal(isDangerousCommand("rm -rf /"), true);
  assert.equal(isDangerousCommand("sudo rm -rf ~/test"), true);
  assert.equal(isDangerousCommand("ls -la"), false);
});

test("runCommand executes normal command", async () => {
  const result = await runCommand({ command: "printf 'ok'", cwd: process.cwd() });

  assert.equal(result.exitCode, 0);
  assert.equal(result.stdout, "ok");
});

test("runCommand returns non-zero safely", async () => {
  const result = await runCommand({ command: "exit 7", cwd: process.cwd() });
  assert.equal(result.exitCode, 7);
});
