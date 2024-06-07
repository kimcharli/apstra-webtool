import { io } from 'socket.io-client';

// "undefined" means the URL will be computed from the `window.location` object
// export NODE_ENV=production
// const URL = process.env.NODE_ENV === 'production' ? undefined : 'https://localhost:8083';

const URL = 'https://localhost:8083';

export const socketEnum = {
    CONNECT: 'connect',
    DISCONNECT: 'disconnect',
    LOGIN: 'login',
    LOGOUT: 'logout',
    SEND_MSG: 'send_msg',
};


// export const socket = io(URL);
export const socket = io(URL, {
    transports: ['websocket', 'polling', 'flashsocket'],
});

