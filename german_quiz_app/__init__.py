import flask
import os
import boto3
import german_quiz_app.config as cfg

dynamodb = boto3.resource("dynamodb", region_name=cfg.AWS_REGION)
table = dynamodb.Table(cfg.DICT_TABLE)
app = flask.Flask(__name__)

# Only enable Flask debugging if an env var is set to true
app.debug = os.environ.get("FLASK_DEBUG") in ["true", "True"]

# Get application version from env
app.config["APP_VERSION"] = os.getenv("APP_VERSION")
app.config['API_ENDPOINT'] = cfg.API_ENDPOINT
app.config["FLASK_ENDPOINT_HOST"] = cfg.FLASK_ENDPOINT_HOST
app.config['FLASK_ENDPOINT_PORT'] = cfg.FLASK_ENDPOINT_PORT

from german_quiz_app import views   

if __name__ == "__main__":
    
    app.run(host=app.config["FLASK_ENDPOINT_HOST"], port=app.config['FLASK_ENDPOINT_PORT'])
