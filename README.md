# 📁 Smart Local File Organizer

A high-performance Full-Stack desktop utility designed to instantly declutter messy directories. Built with a **FastAPI** backend and a **React (Vite)** frontend, this tool organizes files directly on your local machine based on their extensions.

---

## ⚡ Features

* **In-Place Organization:** Unlike web-based tools, this sorts files directly in the source folder. No uploading required.
* **Smart Categorization:** Automatically maps extensions to logical folders:
    * **Images:** .jpg, .png, .svg, .webp
    * **Videos:** .mp4, .mkv, .mov
    * **Documents:** .pdf, .docx, .xlsx, .txt
    * **Code:** .py, .js, .html, .cpp, .json
* **Safety Lock:** Skips sub-folders and system files to prevent data corruption.
* **Collision Handling:** Automatically renames duplicates with timestamps to ensure zero data loss.
* **Live Activity Feed:** A terminal-style log tracks every single file move in real-time.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | React 18, Vite, Tailwind CSS, Lucide Icons |
| **Backend** | Python 3.10+, FastAPI, Uvicorn |
| **Communication** | Axios (REST API) |
| **Logic** | Python Standard Library (`os`, `shutil`) |

---

## ⚙️ Installation & Setup

### 1. Backend (Python)
Navigate to the backend directory and set up the server:
```bash
cd backend
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install fastapi uvicorn pydantic
python main.py
