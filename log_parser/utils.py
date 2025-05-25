import os
import datetime
from pathlib import Path

def normalize_path(path_str):
    """Cross-platform path düzeltici."""
    return str(Path(path_str).expanduser().resolve())

def ensure_dir(path):
    """Klasör varsa geç, yoksa oluştur."""
    Path(path).mkdir(parents=True, exist_ok=True)

def timestamp():
    """Şu anki zamanı YYMMDD_HHMMSS formatında döndürür."""
    return datetime.datetime.now().strftime("%y%m%d_%H%M%S")

def build_report_path(prefix="report", ext="json", output_dir="reports"):
    """Rapor dosyasının benzersiz adını oluşturur."""
    ensure_dir(output_dir)
    name = f"{prefix}_{timestamp()}.{ext}"
    return str(Path(output_dir) / name)

def readable_size(bytes_size):
    """Byte değerini insan okunabilir MB/KB formatında verir."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} TB"
