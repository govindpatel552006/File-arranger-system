import os
import shutil
from config import UPLOAD_DIR, ORGANIZED_DIR
from utils import get_category, get_unique_path

class FileOrganizer:
    @staticmethod
    async def preview_files():
        files = os.listdir(UPLOAD_DIR)
        preview = []
        for f in files:
            preview.append({
                "filename": f,
                "category": get_category(f)
            })
        return preview

    @staticmethod
    async def organize_files():
        files = os.listdir(UPLOAD_DIR)
        logs = []
        
        for f in files:
            source = os.path.join(UPLOAD_DIR, f)
            if os.path.isdir(source): continue
            
            category = get_category(f)
            dest_folder = os.path.join(ORGANIZED_DIR, category)
            os.makedirs(dest_folder, exist_ok=True)
            
            final_path = get_unique_path(os.path.join(dest_folder, f))
            shutil.move(source, final_path)
            logs.append(f"Moved {f} to {category}/")
            
        return logs