content = f"""
// created by script
const ws = new WebSocket("ws://localhost:8000/ws");

ws.onopen = (event) => {{
    console.log('ws.onopen' + event);
    console.log(event);
}};

ws.onmessage = function(event) {{
    event.preventDefault();
    // console.log('ws.onmessage' + event);
    console.log(event);
    const msg = JSON.parse(event.data);
    switch (msg.type) {{
        case 'id-prop-value':
            msg.data.forEach((item) => {{
                const id = item.id;
                const prop = item.prop;
                const value = item.value;
                const attrs = item.attrs
                const element = document.getElementById(id);
                if (element) {{
                    element[prop] = value;
                }}
                attrs.forEach((attr) => {{
                    element.setAttribute(attr.name, attr.value);
                }})
                
            }});
            break;
        default:
            console.log('ws.onmessage: unknown message type: %s', msg.type);            
    }}
}};

ws.onerror = (event) => {{
    console.error('ws.error', event);
}};

ws.onclose = (event) => {{
    console.error('ws.close', event);
}};


function sendMessage(event) {{
    var input = document.getElementById("messageText")
    ws.send(input.value)
    input.value = ''
    event.preventDefault()
}}

function send_form(event) {{
    event.preventDefault();
    const inputs = event.target.form;
    const values = {{}};
    for (const input of inputs) {{
        values[input.name] = input.value;
    }}
    console.log('send_form() sending %O', values)
    ws.send(JSON.stringify(values));
}}

"""