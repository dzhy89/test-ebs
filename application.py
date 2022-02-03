from flask import Flask

application = Flask(__name__)


@application.route("/", methods=["GET"])
def index():
    return "hello world"


if __name__ == "main":
    application.debug = True
    application.run(load_dotenv=True)
