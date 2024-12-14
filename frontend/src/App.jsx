import React, { useState } from "react";

const App = () => {
  const [url, setUrl] = useState("");
  const [formato, setFormato] = useState("mp4");
  const [qualidade, setQualidade] = useState("bestvideo+bestaudio");
  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState(null);
  const [filePath, setFilePath] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setMessage(null);
    setFilePath(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/download/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url, formato, qualidade }),
      });

      const result = await response.json();
      if (response.ok) {
        setMessage("Download concluído com sucesso!");
        setFilePath(result.file_path);
      } else {
        setMessage(`Erro: ${result.detail}`);
      }
    } catch (error) {
      setMessage("Erro ao conectar com o servidor.");
    }

    setIsLoading(false);
  };

  return (
    <div className="bg-gray-100 min-h-screen flex flex-col items-center justify-center">
      <div className="bg-white shadow-md rounded-lg p-6 w-full max-w-md">
        <h1 className="text-2xl font-bold mb-4 text-center">
          YouTube Downloader
        </h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">
              URL do Vídeo
            </label>
            <input
              type="text"
              placeholder="https://www.youtube.com/watch?v=example"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              required
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Formato
            </label>
            <select
              value={formato}
              onChange={(e) => setFormato(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
            >
              <option value="mp4">MP4</option>
              <option value="mp3">MP3</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Qualidade
            </label>
            <select
              value={qualidade}
              onChange={(e) => setQualidade(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
            >
              <option value="bestvideo+bestaudio">Melhor Qualidade</option>
              <option value="bestaudio">Apenas Áudio</option>
              <option value="worst">Qualidade Baixa</option>
            </select>
          </div>
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
          >
            Baixar
          </button>
        </form>
        {isLoading && (
          <p className="text-blue-500 mt-4 text-center">Processando...</p>
        )}
        {message && (
          <p className="text-green-500 mt-4 text-center">{message}</p>
        )}
        {filePath && (
          <div className="mt-4 text-center">
            <a
              href={`http://127.0.0.1:8000/files/${encodeURIComponent(
                filePath
              )}`}
              download
              className="text-blue-700 underline"
            >
              Clique aqui para baixar
            </a>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
