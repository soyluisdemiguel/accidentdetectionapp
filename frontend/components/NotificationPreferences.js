import React, { useState } from 'react';

function NotificationPreferences() {
  const [preferences, setPreferences] = useState({});

  const handlePreferenceChange = (e) => {
    const { name, checked } = e.target;
    setPreferences({ ...preferences, [name]: checked });
  };

  return (
    <div className="notification-preferences">
      <h2>Notification Preferences</h2>
      <div className="preference">
        <input
          type="checkbox"
          name="email"
          onChange={handlePreferenceChange}
        />
        <label htmlFor="email">Email</label>
      </div>
      <div className="preference">
        <input
          type="checkbox"
          name="sms"
          onChange={handlePreferenceChange}
        />
        <label htmlFor="sms">SMS</label>
      </div>
    </div>
  );
}

export default NotificationPreferences;
