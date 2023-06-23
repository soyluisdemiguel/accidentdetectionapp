import React, { useState, useEffect } from 'react';

const NotificationPreferencesManagement = () => {
  const [notificationPreferences, setNotificationPreferences] = useState({});

  useEffect(() => {
    // Reemplazar con una llamada al backend para obtener las preferencias de notificación
    const fetchNotificationPreferences = async () => {
      const response = await fetch('/api/notification-preferences');
      const data = await response.json();
      setNotificationPreferences(data);
    };

    fetchNotificationPreferences();
  }, []);

  return (
    <div>
      <h2>Notification Preferences Management</h2>
      <p>Email Notifications: {notificationPreferences.email ? 'Enabled' : 'Disabled'}</p>
      <p>SMS Notifications: {notificationPreferences.sms ? 'Enabled' : 'Disabled'}</p>
      {/* Render notification preferences form here */}
   
      </div>
  );
};

export default NotificationPreferencesManagement;
