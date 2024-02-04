import React, { useState } from "react";
import axios from "axios";

const ImageComponent = () => {
  const [imageData, setImageData] = useState(null);
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");

  const fetchData = async () => {
    try {
      if (!file || !question) return;

      const formData = new FormData();

      formData.append("question", question);
      formData.append("file", file);
      const response = await axios.post("http://127.0.0.1:8000/api/csv_question/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      console.log(response.data.data, "response");
      setImageData(response.data.data);

    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleQuestionChange = (e) => {
    setQuestion(e.target.value);
  };

  const handleSubmit = () => {
    fetchData();
  };

  return (
    <div>
      <h2>graph</h2>
      <input type="file" onChange={handleFileChange} />
      <input type="text" placeholder="Enter your question" value={question} onChange={handleQuestionChange} />
      <button onClick={handleSubmit}>Submit</button>
      {imageData && (
        <img src={`data:image/png;base64,${imageData}`} alt="Base64 Image" />
      )}
    </div>
  );
};

export default ImageComponent;
