import React, { useEffect, useRef } from 'react';
import L from 'leaflet';

const AccidentMap = () => {
  const mapRef = useRef(null);

  useEffect(() => {
    if (!mapRef.current) {
      return;
    }

    const map = L.map(mapRef.current).setView([51.505, -0.09], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    // Example marker for accident
    L.marker([51.5, -0.09])
      .addTo(map)
      .bindPopup('Accident detected here.')
      .openPopup();

    return () => {
      map.remove();
    };
  }, []);

  return <div id="accident-map" ref={mapRef} style={{ height: '100%', width: '100%' }}></div>;
};

export default AccidentMap;
