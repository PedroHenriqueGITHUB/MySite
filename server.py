from flask import *

server = Flask(__name__)

global logins, passwords
logins = ["sukilovot", "gopnik", "gopher", "pedro", "anderson", "daniel"]
passwords = ["sukilovot7777!", "gopnik7777!", "gopher0000!", "pedro0000!", "anderson1234","daniel12345"]

#login
@server.route("/")
def login():
    return render_template("login.html")

@server.route("/verifylogin", methods=["GET", "POST"])
def verify():
    if request.form["login"] in logins and request.form["password"] in passwords:
        return redirect("homepage")

@server.route("/homepage")
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    server.run(debug=True, port="7545")