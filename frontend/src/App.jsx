import React, { useState } from 'react';
import { uploadFiles, organizeFiles, getPreview } from './api'; // Jo tune pehle banayi thi

function FileCleaner() {
    const [selectedFiles, setSelectedFiles] = useState([]);
    const [status, setStatus] = useState("");

    const handleFileChange = (e) => {
        setSelectedFiles(e.target.files);
    };

    const handleUpload = async () => {
        if (selectedFiles.length === 0) return alert("Pehle files select karo!");
        
        const formData = new FormData();
        for (let i = 0; i < selectedFiles.length; i++) {
            formData.append("files", selectedFiles[i]);
        }

        try {
            setStatus("Uploading...");
            await uploadFiles(formData);
            setStatus("Uploaded! Now organizing...");
            const res = await organizeFiles();
            console.log(res.data.logs);
            setStatus("Done! Check your preview.");
        } catch (err) {
            setStatus("Error: " + err.message);
        }
    };

    return (
        <div className="card">
            <h2>Step 1: Select Files to Clean</h2>
            <input 
                type="file" 
                multiple 
                onChange={handleFileChange} 
                className="file-input"
            />
            
            <button onClick={handleUpload} className="btn-primary">
                🚀 UPLOAD & ORGANIZE
            </button>

            <div className="status-box">
                {status}
            </div>
        </div>
    );
}