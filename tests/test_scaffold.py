"""Smoke tests for every platform adapter, storage independence, and validation."""
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / "scripts/install.py"
VALIDATE = ROOT / "scripts/validate.py"
PLATFORMS = {
    "openai/chatgpt-project": "PROJECT_INSTRUCTIONS.md",
    "openai/codex": "AGENTS.md",
    "anthropic/claude-project": "PROJECT_INSTRUCTIONS.md",
    "anthropic/claude-code": "CLAUDE.md",
    "google/gemini-app": "PROJECT_INSTRUCTIONS.md",
    "google/gemini-cli": "GEMINI.md",
}

class ScaffoldTests(unittest.TestCase):
    def test_every_runtime(self):
        for platform, bootstrap in PLATFORMS.items():
            with self.subTest(platform=platform), TemporaryDirectory() as tmp:
                subprocess.run([sys.executable, str(INSTALL),
                    "--name", "Sample Project", "--slug", "sample",
                    "--platform", platform, "--storage-provider", "github",
                    "--storage-root", "https://example.org/knowledge",
                    "--rules-index-url", "https://example.org/knowledge/agent-rules/INDEX.md",
                    "--output", tmp], check=True, capture_output=True)
                dest = Path(tmp) / "sample"
                self.assertTrue((dest / bootstrap).is_file())
                self.assertIn("https://example.org/knowledge/agent-rules/INDEX.md",
                              (dest / bootstrap).read_text(encoding="utf-8"))
                subprocess.run([sys.executable, str(VALIDATE), str(dest), "--runtime-ready"],
                               check=True, capture_output=True)

    def test_existing_destination_is_not_overwritten(self):
        with TemporaryDirectory() as tmp:
            dest = Path(tmp) / "sample"
            dest.mkdir()
            file = dest / "keep.txt"
            file.write_text("protected")
            result = subprocess.run([sys.executable, str(INSTALL),
                "--name", "Sample", "--slug", "sample",
                "--platform", "google/gemini-cli", "--storage-provider", "google-drive",
                "--output", tmp], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(file.read_text(), "protected")

    def test_missing_runtime_values_fail_validation(self):
        with TemporaryDirectory() as tmp:
            subprocess.run([sys.executable, str(INSTALL),
                "--name", "Sample", "--slug", "sample",
                "--platform", "openai/chatgpt-project", "--storage-provider", "local",
                "--output", tmp], check=True, capture_output=True)
            dest = Path(tmp) / "sample"
            self.assertEqual(subprocess.run([sys.executable, str(VALIDATE), str(dest)],
                            capture_output=True).returncode, 0)
            self.assertNotEqual(subprocess.run([sys.executable, str(VALIDATE),
                            str(dest), "--runtime-ready"], capture_output=True).returncode, 0)

if __name__ == "__main__":
    unittest.main()
