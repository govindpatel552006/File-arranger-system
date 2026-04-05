import axios from 'axios';

const API = axios.create({
    baseURL: 'https://file-arranger-system.onrender.com',
    timeout: 60000, // important for Render (slow wake-up)
});

// ✅ Upload files (VERY IMPORTANT: add headers)
export const uploadFiles = (formData) =>
    API.post('/upload', formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    });

// ✅ Get uploaded files
export const getPreview = () => API.get('/preview');

// ✅ Organize files
export const organizeFiles = () => API.post('/organize');