from hexed import app


@app.route("/")
def index():
    return "Anything really, it works!"
