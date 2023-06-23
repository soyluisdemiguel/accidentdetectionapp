import React, { useState, useEffect } from 'react';

const RealTimeMonitoring = () => {
  const [accidents, setAccidents] = useState([]);

  useEffect(() => {
    // Reemplazar con una llamada al backend para obtener los datos de accidentes en tiempo real
    const fetchAccidents = async () => {
      const response = await fetch('/api/realtime-accidents');
      const data = await response.json();
      setAccidents(data);
    };

    fetchAccidents();
  }, []);

  return (
    <div>
      <h2>Real-time Monitoring</h2>
      <ul>
        {accidents.map((accident) => (
          <li key={accident.id}>
            Accident at {accident.location} - {accident.timestamp}
          </li>
