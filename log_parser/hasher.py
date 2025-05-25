import hashlib
from pathlib import Path

class FileHasher:
    def __init__(self, algorithm="sha256"):
        self.algorithm = algorithm.lower()
        if self.algorithm not in ["sha256", "md5"]:
            raise ValueError("Unsupported hash algorithm. Use 'sha256' or 'md5'.")

    def hash_file(self, file_path: Path) -> str:
        h = hashlib.new(self.algorithm)
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    h.update(chunk)
            return h.hexdigest()
        except Exception as e:
            print(f"[!] Could not hash {file_path}: {e}")
            return ""

    def hash_files(self, files: list[Path]) -> dict:
        results = {}
        for file in files:
            results[str(file)] = self.hash_file(file)
        return results
