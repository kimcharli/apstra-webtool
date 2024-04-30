
content = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Webtool</title>
    <link rel="icon" href="/images/powered-on.svg" />
    <link href="/css/style.css" rel="stylesheet" />
    <script src="/js/main.js"></script>
</head>

<body>

    <section class="log-box">
        <pre id="log-box"></pre>
    </section>

    <div>
        <a href="/"><img style="object-position: left top;" src="/images/home.svg" alt="Home" width="30" height="30"></a>
        <a href="/css/style.css" target="_blank"><img src="/images/css-3.svg" alt="style.css" width="30" height="30"></a>
    </div>

    <div>
        <form id="login-data" action="">
            <table class="border1">
                <tr>
                    <th>version</th>
                    <th>status</th>
                    <th>server</th>
                    <th>port</th>
                    <th>username</th>
                    <th>password</th>
                </tr>
                <tr>
                    <td id="apstra-version"></td>
                    <td id="apstra-status"></td>
                    <td><input type="text" id="apstra-host" name="host" value="10.85.192.45"></td>
                    <td><input type="text" id="apstra-port" name="port" value="443"></td>
                    <td><input type="text" id="apstra-username" name="username" value="admin"></td>
                    <td><input type="password" id="apstra-password" name="password" value="admin"></td>
                </tr>
            </table>
            <input type="hidden" name="command" value="login">
            <button onclick="send_form(event)">Login</button>
        </form>
    </div>

</body>

</html>
"""