from flask import Flask

app =Flask(__name__)

@app.route("/")
def name():
    return "Pradeep S"


@app.route("/registerNumber")
def register_number():
    return "22IT031"

@app.route("/department")
def department():
    return "IT(Information Technology)"

if __name__ == "__main__":
    app.run(debug=True)
