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
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                text-align: center;
            }
            header {
                background-color: #c8102e;
                padding: 20px;
                color: white;
                font-size: 24px;
                font-weight: bold;
            }
            nav {
                background-color: #a50d1f;
                padding: 10px;
            }
            nav a {
                color: white;
                text-decoration: none;
                font-size: 18px;
                margin: 15px;
                padding: 10px 20px;
                display: inline-block;
                transition: background 0.3s;
            }
            nav a:hover {
                background-color: #8c0b1a;
                border-radius: 5px;
            }
            .container {
                max-width: 1000px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }
            h1 {
                color: #c8102e;
            }
            img {
                max-width: 100%;
                border-radius: 10px;
                margin: 15px 0;
            }
            .titles {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 15px;
            }
            .trophy {
                width: 200px;
                text-align: center;
            }
            .trophy img {
                width: 100%;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            }
            .trophy p {
                font-weight: bold;
                margin-top: 10px;
            }
            footer {
                background-color: #c8102e;
                color: white;
                padding: 15px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <header>Liverpool FC - You'll Never Walk Alone</header>
        <nav>
            <a href="/">Home</a>
            <a href="#titles">Trophies</a>
        </nav>

        <div class="container">
            <h1>Welcome to Liverpool FC Fan Page</h1>
            <img src="https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg" alt="Liverpool FC Logo" width="200px">

            <h2>🏆 Major Trophies</h2>
            <div class="titles" id="titles">
                <div class="trophy">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Premier_League_Trophy.png" alt="Premier League Trophy">
                    <p>19x English League Titles</p>
                </div>
                <div class="trophy">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b7/Uefa_cl_trophy.png" alt="Champions League Trophy">
                    <p>6x UEFA Champions League Titles</p>
                </div>
                <div class="trophy">
                    <img src="https://upload.wikimedia.org/wikipedia/en/e/e3/FA_Cup_2013.png" alt="FA Cup Trophy">
                    <p>8x FA Cups</p>
                </div>
                <div class="trophy">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d3/Uefa_Super_Cup.png" alt="UEFA Super Cup Trophy">
                    <p>4x UEFA Super Cups</p>
                </div>
                <div class="trophy">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/FIFA_Club_World_Cup_Trophy.png" alt="FIFA Club World Cup Trophy">
                    <p>1x FIFA Club World Cup</p>
                </div>
            </div>
        </div>

        <footer>
            &copy; 2025 Liverpool FC Fan Page | Created by a Liverpool Supporter
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
