import os
import shutil
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://file-arranger-system-79ts.vercel.app/"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration for sorting
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "PDF_Docs": [".pdf"],
    "Office_Files": [".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".cpp", ".java"],
    "Compressed": [".zip", ".rar", ".7z", ".tar"],
    "Music": [".mp3", ".wav", ".aac"]
}

class PathRequest(BaseModel):
    path: str

@app.post("/organize-in-place")
async def organize_in_place(request: PathRequest):
    folder_path = request.path.strip().strip('"') # Remove quotes if user copied as path
    
    if not os.path.exists(folder_path):
        raise HTTPException(status_code=404, detail="Path not found. Please check the address.")
    
    if not os.path.isdir(folder_path):
        raise HTTPException(status_code=400, detail="This is a file path. Please provide a FOLDER path.")

    # Get all files inside the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        return ["Folder is empty or already organized."]

    logs = []
    for filename in files:
        ext = os.path.splitext(filename)[1].lower()
        source_path = os.path.join(folder_path, filename)
        
        # Decide category
        target_folder_name = "Others"
        for cat, extensions in CATEGORIES.items():
            if ext in extensions:
                target_folder_name = cat
                break
        
        # Create the sub-folder INSIDE the selected folder
        target_dir = os.path.join(folder_path, target_folder_name)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # Move file
        dest_path = os.path.join(target_dir, filename)
        
        # Avoid overwriting if file already exists
        if os.path.exists(dest_path):
            name, extension = os.path.splitext(filename)
            dest_path = os.path.join(target_dir, f"{name}_new{extension}")

        try:
            shutil.move(source_path, dest_path)
            logs.append(f"✓ {filename} → {target_folder_name}/")
        except Exception as e:
            logs.append(f"✗ Failed {filename}: {str(e)}")

    return logs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)