from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
app = Flask(__name__)

#flag="flag{w3b_scr1pt3rs_b3w4re}"

@app.route("/")
def index():
    return "Index!"

@app.route("/register")
def hello():
    if not request.cookies.get('id'):
        id = str(1)
    else:
        id = str(int(request.cookies.get('id')) + 1)
    return render_template("app.html",id=int(id))

@app.route('/createUser', methods = ['POST', 'GET'])
def setCookie():
    if request.method == "POST":

        if not request.cookies.get('id'):
            res = make_response("<script>window.location = \"/register\";</script>")
            res.set_cookie('id', "1")
        else:
            print(request.cookies.get("id"))
            res = make_response("<script>window.location = \"/register\";</script>")
            res.set_cookie('id', str(int(request.cookies.get('id'))+1))
        return res

if __name__ == "__main__":
    app.run()
