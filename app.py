from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1 style="color: #2e7d32;">✅ Cloud App v2.0 is Live!</h1>
            <p>Deploy Time: <strong>{now}</strong></p>
            <p>Environment: <strong>Docker Container</strong></p>
            <hr style="width: 20%; margin: 20px auto;">
            <p>Managed via GitHub & Render</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)