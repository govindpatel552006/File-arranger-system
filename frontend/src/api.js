import axios from 'axios';

const API = axios.create({
    baseURL: 'https://file-arranger-system.onrender.com',
});

export const uploadFiles = (formData) => API.post('/upload', formData);
export const getPreview = () => API.get('/preview');
export const organizeFiles = () => API.post('/organize');