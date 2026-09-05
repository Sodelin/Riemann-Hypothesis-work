"""Regression coverage for verification with assertions disabled."""

import os
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECKERS = ('code/theta_slice_interval_certificate.py',)


class AssertionModeTests(unittest.TestCase):
    def test_optimized_modes_refuse_verification(self):
        for checker in CHECKERS:
            for option in ("-O", "-OO", "PYTHONOPTIMIZE"):
                with self.subTest(checker=checker, option=option):
                    env = os.environ.copy()
                    env.pop("PYTHONOPTIMIZE", None)
                    flags = []
                    if option == "PYTHONOPTIMIZE":
                        env[option] = "1"
                    else:
                        flags = [option]
                    result = subprocess.run(
                        [sys.executable, "-B", *flags, str(ROOT / checker)],
                        cwd=ROOT,
                        env=env,
                        capture_output=True,
                        text=True,
                        timeout=15,
                    )
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn("Verification requires assertions", result.stderr)
                    self.assertNotIn("PASS", result.stdout)
                    self.assertNotIn("CERTIFIED", result.stdout)


if __name__ == "__main__":
    unittest.main()
