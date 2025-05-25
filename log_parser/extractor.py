import os
import zipfile
import rarfile
import tempfile
from pathlib import Path

class LogExtractor:
    def __init__(self, archive_path):
        self.archive_path = Path(archive_path)
        self.extract_dir = Path(tempfile.mkdtemp(prefix="log_extract_"))

    def extract(self):
        if self.archive_path.suffix == ".zip":
            self._extract_zip()
        elif self.archive_path.suffix == ".rar":
            self._extract_rar()
        else:
            raise ValueError(f"Unsupported archive format: {self.archive_path.suffix}")

        return self.extract_dir

    def _extract_zip(self):
        with zipfile.ZipFile(self.archive_path, 'r') as zip_ref:
            zip_ref.extractall(self.extract_dir)

    def _extract_rar(self):
        with rarfile.RarFile(self.archive_path, 'r') as rar_ref:
            rar_ref.extractall(self.extract_dir)

    def list_files(self):
        return [str(p) for p in self.extract_dir.rglob("*") if p.is_file()]
