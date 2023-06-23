import React, { useEffect, useState } from 'react';

const EmergencyContacts = () => {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    // Reemplazar con una llamada al backend para obtener los contactos de emergencia
    const fetchContacts = async () => {
      const response = await fetch('/api/emergency-contacts');
      const data = await response.json();
      setContacts(data);
    };

    fetchContacts();
  }, []);

  return (
    <div>
      <h2>Emergency Contacts</h2>
      <ul>
        {contacts.map((contact) => (
          <li key={contact.id}>
            {contact.name} - {contact.phone}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmergencyContacts;
