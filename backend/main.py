import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# ✅ CORS FIX (no trailing slash)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://file-arranger-system-64v5u25q7.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Folder where uploaded files will be stored
UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# File categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "PDF_Docs": [".pdf"],
    "Office_Files": [".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".cpp", ".java"],
    "Compressed": [".zip", ".rar", ".7z", ".tar"],
    "Music": [".mp3", ".wav", ".aac"]
}

# ✅ 1️⃣ Upload Files API
@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    uploaded_files = []

    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        uploaded_files.append(file.filename)

    return {
        "message": "Files uploaded successfully",
        "files": uploaded_files
    }

# ✅ 2️⃣ Preview Files API
@app.get("/preview")
async def preview_files():
    files = os.listdir(UPLOAD_DIR)
    return {"files": files}

# ✅ 3️⃣ Organize Files API
@app.post("/organize")
async def organize_files():
    files = os.listdir(UPLOAD_DIR)
    
    if not files:
        return {"message": "No files to organize"}

    logs = []

    for filename in files:
        source_path = os.path.join(UPLOAD_DIR, filename)

        if not os.path.isfile(source_path):
            continue

        ext = os.path.splitext(filename)[1].lower()

        # Find category
        category = "Others"
        for cat, extensions in CATEGORIES.items():
            if ext in extensions:
                category = cat
                break

        target_dir = os.path.join(UPLOAD_DIR, category)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        dest_path = os.path.join(target_dir, filename)

        # Avoid overwrite
        if os.path.exists(dest_path):
            name, extension = os.path.splitext(filename)
            dest_path = os.path.join(target_dir, f"{name}_new{extension}")

        try:
            shutil.move(source_path, dest_path)
            logs.append(f"✓ {filename} → {category}/")
        except Exception as e:
            logs.append(f"✗ {filename}: {str(e)}")

    return {"logs": logs}

# ✅ Root API (for testing)
@app.get("/")
async def root():
    return {"message": "Backend is running 🚀"}

# ✅ For local run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)