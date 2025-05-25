import sys
import json
from pathlib import Path

from log_parser.extractor import LogExtractor
from log_parser.classifier import LogClassifier
from log_parser.ioc_finder import IOCFinder
from log_parser.hasher import FileHasher
from log_parser.utils import build_report_path, normalize_path

def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py <log_archive.zip/rar>")
        sys.exit(1)

    archive_path = normalize_path(sys.argv[1])
    if not Path(archive_path).exists():
        print(f"[!] File not found: {archive_path}")
        sys.exit(1)

    print(f"📦 Processing archive: {archive_path}")
    extractor = LogExtractor(archive_path)
    extract_dir = extractor.extract()
    print(f"📂 Extracted to: {extract_dir}")

    classifier = LogClassifier(extract_dir)
    classified = classifier.classify()

    ioc_finder = IOCFinder()
    hasher = FileHasher("sha256")

    report = {
        "source_archive": str(archive_path),
        "extracted_path": str(extract_dir),
        "hashes": {},
        "iocs": {}
    }

    all_files = [f for sublist in classified.values() for f in sublist]
    report["hashes"] = hasher.hash_files(all_files)

    for category, files in classified.items():
        if files:
            iocs = ioc_finder.extract_from_files(files)
            report["iocs"][category] = iocs

    report_path = build_report_path(prefix="ioc_report", ext="json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print(f"✅ IOC report saved to: {report_path}")
