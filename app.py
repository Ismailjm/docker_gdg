from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello GDG I was Dockerized 🐋</h2>'


if __name__ == "__main__":
    app.run(debug=True)