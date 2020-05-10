from german_quiz_app import app
from german_quiz_app import config as cfg


if __name__ == "__main__":
    app.run(host=app.config['FLASK_ENDPOINT_HOST'], port=app.config['FLASK_ENDPOINT_PORT'])