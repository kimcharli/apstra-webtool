import React, { useState, useCallback, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx'
import './index.css';
import ApstraServer from './components/ApstraServer.jsx';
import GenericSystem from './components/GenericSystem.jsx';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
  <div>Hello World</div>
    <App />
    <ApstraServer />
    <GenericSystem />
  </React.StrictMode>,
)
