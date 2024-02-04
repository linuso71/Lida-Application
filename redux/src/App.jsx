import React, { useEffect, useState } from "react";

const ImageComponent = () => {
  const [imageData, setImageData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/csv_question/", {
          method: 'POST',
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        setImageData(data);
      } catch (error) {
        console.error('Error fetching data:', error);
        // Handle error as needed
      }
    };

    fetchData();
  }, []);

  return (
    <div><h2>image</h2>

      {imageData && (
        <img src={`data:image/png;base64,${imageData}`} alt="Base64 Image" />
      )}
    </div>
  );
};

export default ImageComponent;