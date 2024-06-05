// import React, { useState } from 'react';
import './ApstraServer.css';
import { useState } from 'react';
import { socket } from '../socket';

export default function ApstraServer() {
  const [version, setVersion] = useState('0.0.0');
  const [loginAction, setLoginAction] = useState('Login');
  const [status, setStatus] = useState('None');
  const [host, setHost] = useState('10.85.192.45');
  const [port, setPort] = useState('443');
  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('admin');

  const handleLogin = (event) => {
    event.preventDefault();

    // Simulate connection logic
    if (host && port && username && password) {
      if (loginAction === 'Login') {
        socket.emit('login', { host, port, username, password });
        socket.on('login', (data) => {
          setVersion(data.version);
          setStatus(data.status);
        });
        setLoginAction('Logout');
      } else {
        socket.emit('logout');
        setVersion('0.0.0');
        setStatus('Disconnected');
        setLoginAction('Login');
      }
    } else {
      setStatus('Connection Failed');
    }
  };

  return (
    <>
      <form id="login-data" onSubmit={handleLogin}>
        <button type="submit">{loginAction}</button>
        <label className="login-status">{status}</label>

        <label className="label-version header" htmlFor="version">version</label>
        <label className="text-version">{version}</label>

        <label className="label-host header" htmlFor="host">host</label>
        <label className="label-port header" htmlFor="port">port</label>
        <label className="label-username header" htmlFor="username">username</label>
        <label className="label-password header" htmlFor="password">password</label>

        <input className="input-host" type="text" id="apstra-host" name="host" value={host} onChange={(e) => setHost(e.target.value)} required />
        <input className="input-port" type="text" id="apstra-port" name="port" value={port} onChange={(e) => setPort(e.target.value)} required />
        <input className="input-username" type="text" id="apstra-username" name="username" value={username} onChange={(e) => setUsername(e.target.value)} required />
        <input className="input-password" type="password" id="apstra-password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} required />

      </form>
    </>
  );
}

