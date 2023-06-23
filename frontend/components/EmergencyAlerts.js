import React, { useState } from 'react';

function EmergencyAlerts() {
  const [alertSent, setAlertSent] = useState(false);

  const handleSendAlert = () => {
    // TODO: Call the appropriate API endpoint to send the emergency alert
    setAlertSent(true);
  };

  return (
    <div className="emergency-alerts">
      <h2>Emergency Alerts</h2>
      {alertSent ? (
        <p>Emergency alert has been sent to the relevant services.</p>
      ) : (
        <div>
          <p>Click the button below to send an emergency alert.</p>
          <button onClick={handleSendAlert}>Send Emergency Alert</button>
        </div>
      )}
    </div>
  );
}

export default EmergencyAlerts;
