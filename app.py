from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>CI/CD Pipeline</title>
    </head>
    <body>
        <h1>Welcome to CI/CD Pipeline!</h1>
        <h2>GitHub Actions + Docker + Flask</h2>
        <h3>Application Successfully Deployed!</h3>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "Application is Healthy!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)