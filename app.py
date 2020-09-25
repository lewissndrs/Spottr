from flask import Flask,render_template

# import various controllers

app = Flask(__name__)

# register blueprints

@app.route("/")
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run