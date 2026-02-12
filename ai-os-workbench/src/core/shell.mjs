import { exec } from "node:child_process";
import { promisify } from "node:util";

const execAsync = promisify(exec);

const dangerPatterns = [
  /\brm\s+-rf\b/i,
  /\brm\s+-fr\b/i,
  /\bmkfs\b/i,
  /\bdd\s+if=/i,
  /\bshutdown\b/i,
  /\breboot\b/i,
  /\bkillall\s+-9\b/i,
  /:\(\)\s*\{\s*:\|:&\s*\};:/,
  /\bsudo\s+rm\b/i,
  /\bchown\s+-R\s+root\b/i
];

export function isDangerousCommand(command) {
  return dangerPatterns.some((pattern) => pattern.test(command));
}

export async function runCommand({ command, cwd, allowUnsafe = false, timeoutMs = 20_000 }) {
  if (!allowUnsafe && isDangerousCommand(command)) {
    const error = new Error("Command blocked by safety policy. Toggle 'Allow unsafe commands' to bypass.");
    error.code = "COMMAND_BLOCKED";
    throw error;
  }

  const startedAt = Date.now();

  try {
    const { stdout, stderr } = await execAsync(command, {
      cwd,
      timeout: timeoutMs,
      shell: "/bin/zsh",
      maxBuffer: 2 * 1024 * 1024
    });

    return {
      stdout,
      stderr,
      exitCode: 0,
      durationMs: Date.now() - startedAt
    };
  } catch (error) {
    return {
      stdout: error.stdout || "",
      stderr: error.stderr || error.message,
      exitCode: Number.isInteger(error.code) ? error.code : 1,
      durationMs: Date.now() - startedAt
    };
  }
}
