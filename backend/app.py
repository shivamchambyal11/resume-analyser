from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Resume Analyzer Backend Running 🚀"

if __name__ == "__main__":
    app.run(debug=True)