import os
from dotenv import load_dotenv

load_dotenv()

DICT_TABLE = "german_quiz"
AWS_REGION = "eu-central-1"

FLASK_ENDPOINT_HOST = os.getenv('FLASK_ENDPOINT_HOST', '0.0.0.0')
FLASK_ENDPOINT_PORT = os.getenv('FLASK_ENDPOINT_PORT', 5000)
API_ENDPOINT = os.getenv('API_ENDPOINT', "http://germanwordquiz-env.eba-5pjscnfr.eu-central-1.elasticbeanstalk.com")