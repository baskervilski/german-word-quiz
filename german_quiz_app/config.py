import os

DICT_TABLE = "german_quiz"
AWS_REGION = "eu-central-1"

FLASK_ENDPOINT_HOST = os.getenv('FLASK_ENDPOINT_HOST', '0.0.0.0')
FLASK_ENDPOINT_PORT = os.getenv('FLASK_ENDPOINT_PORT', 5000)
API_ENDPOINT = os.getenv('API_ENDPOINT', "0.0.0.0:5000")