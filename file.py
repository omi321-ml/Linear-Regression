from flask import Flask

file=Flask(__name__)
@file.route("/")

def home():
    return "This is my bari"

@file.route("/welcome")
def wel():
    return "Welcome my server"
if __name__=="__main__":
    file.run(debug=True)

