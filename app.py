from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/result1", methods=["POST"])
def result1():
    name = request.form.get("name")
    email = request.form.get("email")

    return render_template("result1.html", name=name, email=email)



if __name__ == '__main__':
    app.run(debug=True)
