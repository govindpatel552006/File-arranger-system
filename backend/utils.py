import os
import time

def get_unique_path(path):
    """Prevents overwriting by adding a timestamp if file exists."""
    if not os.path.exists(path):
        return path
    
    filename, extension = os.path.splitext(path)
    return f"{filename}_{int(time.time())}{extension}"

def get_category(filename):
    from config import FILE_CATEGORIES
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"