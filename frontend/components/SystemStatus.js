import React, { useState, useEffect } from 'react';

const SystemStatus = () => {
  const [systemStatus, setSystemStatus] = useState({});

  useEffect(() => {
    // Reemplazar con una llamada al backend para obtener el estado del sistema
    const fetchSystemStatus = async () => {
      const response = await fetch('/api/system-status');
      const data = await response.json();
      setSystemStatus(data);
    };

    fetchSystemStatus();
  }, []);

  return (
    <div>
      <h2>System Status</h2>
      <p>CPU Usage: {systemStatus.cpu_usage}%</p>
      <p>Memory Usage: {systemStatus.memory_usage}%</p>
      <p>Disk Usage: {systemStatus.disk_usage}%</p>
    </div>
  );
};

export default SystemStatus;