import React, { useState } from 'react';
import axios from 'axios';
import { FolderUp, Play, Terminal, CheckCircle, Loader2, AlertTriangle } from 'lucide-react';

export default function App() {
  const [folderPath, setFolderPath] = useState("");
  const [logs, setLogs] = useState(["Waiting for folder path..."]);
  const [loading, setLoading] = useState(false);

  const startOrganizing = async () => {
    if (!folderPath) return alert("Please enter a path!");
    
    setLoading(true);
    setLogs(["Initializing cleanup..."]);

    try {
      const response = await axios.post('http://localhost:8000/organize-in-place', {
        path: folderPath
      });

      setLogs(response.data);
    } catch (err) {
      const msg = err.response?.data?.detail || "Connection Error. Is Backend running?";
      setLogs([`ERROR: ${msg}`]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#050505] text-slate-200 flex items-center justify-center p-4">
      <div className="w-full max-w-4xl bg-[#0f0f0f] border border-white/10 rounded-3xl shadow-2xl overflow-hidden">
        
        <div className="p-8 border-b border-white/5 bg-gradient-to-b from-white/[0.02] to-transparent">
          <h1 className="text-3xl font-black bg-gradient-to-r from-blue-400 to-indigo-500 bg-clip-text text-transparent mb-2">
            LOCAL FOLDER CLEANER
          </h1>
          <p className="text-slate-500 text-sm">Sort files into sub-folders instantly on your hard drive.</p>
        </div>

        <div className="p-8 grid grid-cols-1 md:grid-cols-2 gap-8">
          
          <div className="space-y-6">
            <div className="bg-white/5 p-6 rounded-2xl border border-white/5">
              <label className="text-xs font-bold text-slate-500 uppercase tracking-widest block mb-3">
                1. Paste Folder Path
              </label>
              <input 
                type="text" 
                placeholder="C:\Users\Downloads\MessyFolder" 
                value={folderPath}
                onChange={(e) => setFolderPath(e.target.value)}
                className="w-full bg-black border border-white/10 rounded-xl p-4 text-blue-400 placeholder:text-slate-800 focus:border-blue-500 outline-none transition-all mb-4"
              />
              
              <div className="flex items-start gap-3 p-3 bg-blue-500/5 rounded-xl border border-blue-500/10 mb-6">
                <AlertTriangle className="text-blue-500 shrink-0" size={16} />
                <p className="text-[10px] text-slate-400 leading-tight">
                  Go to your folder in Windows, click the top address bar, copy it, and paste it here.
                </p>
              </div>

              <button 
                onClick={startOrganizing}
                disabled={loading}
                className="w-full bg-blue-600 hover:bg-blue-500 py-4 rounded-xl font-black text-lg flex items-center justify-center gap-3 active:scale-95 transition-all disabled:opacity-50"
              >
                {loading ? <Loader2 className="animate-spin" /> : <><Play size={20} fill="currentColor"/> CLEAN FOLDER NOW</>}
              </button>
            </div>
          </div>

          <div className="flex flex-col bg-black rounded-2xl border border-white/5 overflow-hidden">
            <div className="px-4 py-3 border-b border-white/5 bg-white/5 flex items-center gap-2">
              <Terminal size={14} className="text-slate-500" />
              <span className="text-[10px] font-bold text-slate-500 uppercase">Live Progress</span>
            </div>
            
            <div className="flex-1 p-5 font-mono text-[11px] overflow-y-auto max-h-[300px] space-y-1 custom-scrollbar text-slate-500">
              {logs.map((log, i) => (
                <div key={i} className={log.includes("✓") ? "text-emerald-500" : log.includes("ERROR") ? "text-red-500" : ""}>
                   {log}
                </div>
              ))}
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}