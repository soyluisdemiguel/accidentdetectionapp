import React, { useState, useEffect } from 'react';

const SensorSettings = () => {
  const [sensorSettings, setSensorSettings] = useState([]);

  useEffect(() => {
    // Reemplazar con una llamada al backend para obtener la configuración de los sensores
    const fetchSensorSettings = async () => {
      const response = await fetch('/api/sensor-settings');
      const data = await response.json();
      setSensorSettings(data);
    };

    fetchSensorSettings();
  }, []);

  return (
    <div>
      <h2>Sensor Settings</h2>
      <ul>
        {sensorSettings.map((sensor) => (
          <li key={sensor.id}>
            {sensor.name} - {sensor.status ? 'Enabled' : 'Disabled'}
          </li>
        ))}
      </ul>
      {/* Render sensor settings form here */}
    </div>
  );
};

export default SensorSettings;
