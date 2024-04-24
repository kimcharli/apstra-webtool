
const ws = new WebSocket("ws://localhost:8000/ws");

ws.open = (event) => {
    console.log('ws.open' + event);
    console.log(event);
};

ws.onmessage = function(event) {
    event.preventDefault();
    // console.log('ws.onmessage' + event);
    console.log(event);
};

ws.onerror = (event) => {
    console.error('ws.error', event);
};

ws.onclose = (event) => {
    console.error('ws.close', event);
};


function sendMessage(event) {
    var input = document.getElementById("messageText")
    ws.send(input.value)
    input.value = ''
    event.preventDefault()
}

function connect(event) {
    event.preventDefault();
    const inputs = event.target.form;
    const values = {};
    for (const input of inputs) {
        values[input.name] = input.value;
    }
    console.log('connect() sending %O', values)
    ws.send(JSON.stringify(values));
}
