from flask import Flask, make_response, jsonify

application = Flask(__name__)


@application.route("/", methods=["GET"])
def app():
    return make_response(jsonify({"message": "hello world"}))


if __name__ == "__main__":
    application.run()
