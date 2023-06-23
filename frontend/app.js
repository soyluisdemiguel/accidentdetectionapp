import React from 'react';
import ReactDOM from 'react-dom';
import AccidentMap from './components/AccidentMap';
import ArduinoControl from './components/ArduinoControl';
import EmergencyAlerts from './components/EmergencyAlerts';
import AnalyticsDashboard from './components/AnalyticsDashboard';

function App() {
  return (
    <div className="app">
      <h1>Accident Detection App</h1>
      <div className="app-container">
        <div className="accident-map-container">
          <AccidentMap />
        </div>
        <div className="arduino-control-container">
          <ArduinoControl />
        </div>
        <div className="analytics-dashboard-container">
          <AnalyticsDashboard />
        </div>
        <div className="emergency-alerts-container">
          <EmergencyAlerts />
        </div>
      </div>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));