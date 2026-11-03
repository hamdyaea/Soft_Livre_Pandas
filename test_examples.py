# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import unittest


class ExamplesTests(unittest.TestCase):
    def test_all_chapters_from_unrelated_directory(self):
        root = Path(__file__).resolve().parent
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "examples"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            examples = sorted(copy.glob("Chapitre*/*.py"))
            self.assertEqual(len(examples), 31)
            for source in examples:
                with self.subTest(example=source.relative_to(copy)):
                    result = subprocess.run(
                        ["python3", str(source)], cwd=temp,
                        env=dict(os.environ, MPLBACKEND="Agg"),
                        capture_output=True, text=True, timeout=30)
                    self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
