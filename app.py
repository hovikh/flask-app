from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Liverpool FC</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
            }
            h1 {
                color: #c8102e;
            }
            img {
                width: 200px;
                margin-top: 20px;
            }
            .info {
                max-width: 600px;
                margin: auto;
                padding: 20px;
                text-align: left;
                background: white;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            .info p {
                font-size: 16px;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Liverpool FC Fan Page</h1>
        <img src="https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg" alt="Liverpool FC Logo">
        <p>You’ll Never Walk Alone</p>

        <div class="info">
            <h2>About Liverpool FC</h2>
            <p><strong>Founded:</strong> 3 June 1892</p>
            <p><strong>Stadium:</strong> Anfield (Capacity: 53,394)</p>
            <p><strong>Manager:</strong> Jürgen Klopp</p>
            <p><strong>League:</strong> English Premier League</p>
            <p><strong>Achievements:</strong></p>
            <ul>
                <li>19x English League Titles</li>
                <li>6x UEFA Champions League Titles</li>
                <li>8x FA Cups</li>
                <li>4x UEFA Super Cups</li>
                <li>1x FIFA Club World Cup</li>
            </ul>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
