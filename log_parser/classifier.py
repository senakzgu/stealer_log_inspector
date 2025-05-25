from pathlib import Path

class LogClassifier:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.classified = {
            "passwords": [],
            "cookies": [],
            "wallets": [],
            "system_info": [],
            "browsers": [],
            "clipboard": [],
            "tokens": [],
            "tdata": [],
            "other": []
        }

    def classify(self):
        for file_path in self.base_dir.rglob("*"):
            if file_path.is_file():
                name = file_path.name.lower()

                if "password" in name:
                    self.classified["passwords"].append(file_path)
                elif "cookie" in name:
                    self.classified["cookies"].append(file_path)
                elif "wallet" in name and file_path.suffix == ".json":
                    self.classified["wallets"].append(file_path)
                elif "system_info" in name:
                    self.classified["system_info"].append(file_path)
                elif "browser" in name or file_path.suffix == ".log":
                    self.classified["browsers"].append(file_path)
                elif "clipboard" in name:
                    self.classified["clipboard"].append(file_path)
                elif "token" in name:
                    self.classified["tokens"].append(file_path)
                elif "tdata" in name or "telegram" in file_path.parts:
                    self.classified["tdata"].append(file_path)
                else:
                    self.classified["other"].append(file_path)

        return self.classified
