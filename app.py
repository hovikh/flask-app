from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
       
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
            .info {
                text-align: left;
                font-size: 18px;
                line-height: 1.6;
            }
            .titles, .legends {
                list-style: none;
                padding: 0;
            }
            .titles li, .legends li {
                background: #c8102e;
                color: white;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                text-align: center;
                font-weight: bold;
            }
            .history {
                background: #f1f1f1;
                padding: 20px;
                border-radius: 10px;
                text-align: left;
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
            <a href="#history">History</a>
            <a href="#titles">Trophies</a>
            <a href="#legends">Legends</a>
            <a href="#managers">Managers</a>
        </nav>

        <div class="container">
            <h1>Welcome to Liverpool FC Fan Page</h1>
            <img src="https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg" alt="Liverpool FC Logo" width="200px">
            
            <h2>🏟️ Anfield Stadium</h2>
            <img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Anfield_Stadium.jpg" alt="Anfield Stadium">
            
            <div class="info">
                <h2>About Liverpool FC</h2>
                <p><strong>Founded:</strong> 3 June 1892</p>
                <p><strong>Stadium:</strong> Anfield (Capacity: 53,394)</p>
                <p><strong>Manager:</strong> Jürgen Klopp</p>
                <p><strong>League:</strong> English Premier League</p>
            </div>

            <div class="history" id="history">
                <h2>Club History 📜</h2>
                <p>Liverpool FC was founded in 1892 after a dispute between Everton FC and their stadium owner. The club quickly rose to prominence, winning its first league title in 1901. The golden era of the 1970s and 80s saw Liverpool dominate English and European football under Bill Shankly, Bob Paisley, and Kenny Dalglish.</p>
                <p>In 2005, Liverpool staged the famous "Miracle of Istanbul" comeback against AC Milan to win their 5th UEFA Champions League title. In 2019, under Jürgen Klopp, they won their 6th Champions League and, in 2020, claimed their first English league title in 30 years.</p>
            </div>

            <div class="info" id="titles">
                <h2>🏆 Major Trophies</h2>
                <ul class="titles">
                    <li>🏆 19x English League Titles</li>
                    <li>🏆 6x UEFA Champions League Titles</li>
                    <li>🏆 8x FA Cups</li>
                    <li>🏆 4x UEFA Super Cups</li>
                    <li>🏆 1x FIFA Club World Cup</li>
                </ul>
            </div>

            <div class="info" id="legends">
                <h2>⚽ Legendary Players</h2>
                <ul class="legends">
                    <li>Steven Gerrard 🏅</li>
                    <li>Kenny Dalglish 🔥</li>
                    <li>Ian Rush 🎯</li>
                    <li>Mohamed Salah ⚡</li>
                    <li>Fernando Torres 🚀</li>
                    <li>Robbie Fowler 🎯</li>
                </ul>
            </div>

            <div class="info" id="managers">
                <h2>👔 Notable Managers</h2>
                <ul class="titles">
                    <li>Bill Shankly (1959-1974) 🔥</li>
                    <li>Bob Paisley (1974-1983) 🏆</li>
                    <li>Kenny Dalglish (1985-1991, 2011-2012) 🎯</li>
                    <li>Rafael Benítez (2004-2010) ✨</li>
                    <li>Jürgen Klopp (2015-Present) 🌟</li>
                </ul>
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
