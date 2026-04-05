from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from organizer import FileOrganizer

router = APIRouter()

class FolderPath(BaseModel):
    path: str

@router.post("/organize-local")
async def organize_local_folder(data: FolderPath):
    # Check if the folder exists on your computer
    if not os.path.exists(data.path):
        raise HTTPException(status_code=404, detail="Directory not found")
    
    # Use our logic to organize that specific folder
    files = os.listdir(data.path)
    logs = []
    
    # Categories mapping
    categories = {
        "Photos": [".jpg", ".jpeg", ".png", ".gif"],
        "PDF_Documents": [".pdf"],
        "Docs": [".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".mov", ".mkv"]
    }

    for f in files:
        source_path = os.path.join(data.path, f)
        if os.path.isdir(source_path): continue
        
        ext = os.path.splitext(f)[1].lower()
        target_folder = "Others"
        
        for cat, exts in categories.items():
            if ext in exts:
                target_folder = cat
                break
        
        dest_dir = os.path.join(data.path, target_folder)
        os.makedirs(dest_dir, exist_ok=True)
        
        try:
            import shutil
            shutil.move(source_path, os.path.join(dest_dir, f))
            logs.append(f"Moved {f} -> {target_folder}/")
        except Exception as e:
            logs.append(f"Failed to move {f}: {str(e)}")
            
    return logs