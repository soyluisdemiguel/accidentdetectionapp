import React, { useState, useEffect } from 'react';

const ModelConfiguration = () => {
  const [modelConfig, setModelConfig] = useState({});

  useEffect(() => {
    // Reemplazar con una llamada al backend para obtener la configuración del modelo
    const fetchModelConfig = async () => {
      const response = await fetch('/api/model-config');
      const data = await response.json();
      setModelConfig(data);
    };

    fetchModelConfig();
  }, []);

  return (
    <div>
      <h2>Model Configuration</h2>
      <p>Model Version: {modelConfig.version}</p>
      <p>Model Threshold: {modelConfig.threshold}</p>
      {/* Render model configuration form here */}
    </div>
  );
};

export default ModelConfiguration;
