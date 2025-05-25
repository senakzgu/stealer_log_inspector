import re
from pathlib import Path

class IOCFinder:
    def __init__(self):
        # Regex desenleri
        self.patterns = {
            "emails": re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
            "btc_wallets": re.compile(r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b"),
            "eth_wallets": re.compile(r"\b0x[a-fA-F0-9]{40}\b"),
            "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
            "tokens": re.compile(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"),
        }

    def extract_from_file(self, file_path: Path) -> dict:
        iocs = {key: [] for key in self.patterns}
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for key, pattern in self.patterns.items():
                    matches = pattern.findall(content)
                    if matches:
                        iocs[key].extend(matches)
        except Exception as e:
            print(f"[!] Could not read file {file_path}: {e}")
        return iocs

    def extract_from_files(self, files: list[Path]) -> dict:
        final_iocs = {key: set() for key in self.patterns}

        for file in files:
            iocs = self.extract_from_file(file)
            for key in final_iocs:
                final_iocs[key].update(iocs[key])

        # Set → List
        return {key: list(val) for key, val in final_iocs.items()}
