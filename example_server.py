from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def get():
    return "Hello from Vserver!"

@app.post("/")
def post():
    print(request.form)
    return "POST Received!"


app.run(port=8000)