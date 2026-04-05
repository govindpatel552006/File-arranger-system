import os

UPLOAD_DIR = "uploads"
ORGANIZED_DIR = "organized"

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(ORGANIZED_DIR, exist_ok=True)

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".json", ".ts"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
}