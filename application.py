from german_quiz_app import app
from german_quiz_app import config as cfg

if __name__ == "__main__":
    app.run(host=cfg.FLASK_ENDPOINT_HOST, port=cfg.FLASK_ENDPOINT_PORT)