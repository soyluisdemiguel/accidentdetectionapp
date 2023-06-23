// frontend/components/AlertSettings.js

import React, { useState } from 'react';

const AlertSettings = () => {
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePhoneNumberChange = (e) => {
    setPhoneNumber(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Email: ${email}, Phone Number: ${phoneNumber}`);
    // Aquí puedes añadir la lógica para guardar las configuraciones de alerta.
  };

  return (
    <div className="alert-settings">
      <h2>Alert Settings</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={handleEmailChange}
        />
        <br />
        <label htmlFor="phone-number">Phone Number:</label>
        <input
          type="tel"
          id="phone-number"
          value={phoneNumber}
          onChange={handlePhoneNumberChange}
        />
        <br />
        <button type="submit">Save</button>
      </form>
    </div>
  );
};

export default AlertSettings;
