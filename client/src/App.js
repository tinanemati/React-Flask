import { useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [files, setFiles] = useState(null);
  const [msg, setMsg] = useState(null);

  function handleUpload() {
    if (!files) {
      setMsg("No File Selected");
      return;
    }

    const fd = new FormData();
    for (let i = 0; i < files.length; i++) {
      fd.append("file", files[i]);
    }

    setMsg("Uploading...");
    axios
      .post("http://127.0.0.1:5000/upload", fd, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((res) => {
        setMsg("Upload successful");
        console.log(res.data);
      })
      .catch((err) => {
        setMsg("Upload failed");
        console.error(err);
      });
  }
  return (
    <div className="App">
      <h1> Uploading Files in React</h1>

      <input
        onChange={(e) => {
          setFiles(e.target.files);
        }}
        type="file"
        multiple
  
      />

      <button onClick={handleUpload}>Upload</button>

      {msg && <span>{msg}</span>}
    </div>
  );
}

export default App;
