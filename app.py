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
        </style>
    </head>
    <body>
        <h1>Welcome to Liverpool FC Fan Page</h1>
        <img src="https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg" alt="Liverpool FC Logo">
        <p>You’ll Never Walk Alone</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
