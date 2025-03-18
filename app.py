from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Liverpool FC - You'll Never Walk Alone</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
            }
            h1 {
                color: #c8102e;
                margin-top: 20px;
            }
            img {
                width: 300px;
                margin: 20px;
            }
            .info {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                text-align: left;
                background: white;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            .info p, .info ul {
                font-size: 16px;
                line-height: 1.6;
            }
            .info ul {
                list-style: none;
                padding: 0;
            }
            .info ul li {
                background: #c8102e;
                color: white;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Liverpool FC Fan Page</h1>
        
        <img src="https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg" alt="Liverpool FC Logo">
        
        <h2>You’ll Never Walk Alone</h2>
        
        <img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Anfield_Stadium.jpg" width="600px" alt="Anfield Stadium">

        <div class="info">
            <h2>About Liverpool FC</h2>
            <p><strong>Founded:</strong> 3 June 1892</p>
            <p><strong>Stadium:</strong> Anfield (Capacity: 53,394)</p>
            <p><strong>Manager:</strong> Jürgen Klopp</p>
            <p><strong>League:</strong> English Premier League</p>

            <h2>Major Titles</h2>
            <ul>
                <li>19x English League Titles 🏆</li>
                <li>6x UEFA Champions League Titles 🏆</li>
                <li>8x FA Cups 🏆</li>
                <li>4x UEFA Super Cups 🏆</li>
                <li>1x FIFA Club World Cup 🏆</li>
            </ul>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
