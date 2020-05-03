import flask
import os

app = flask.Flask(__name__)

# Only enable Flask debugging if an env var is set to true
app.debug = os.environ.get('FLASK_DEBUG') in ['true', 'True']

# Get application version from env
app.config['APP_VERSION'] = os.environ.get('APP_VERSION')

# Get cool new feature flag from env
app.config['enable_cool_new_feature'] = os.environ.get('ENABLE_COOL_NEW_FEATURE') in ['true', 'True']

from . import views
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')
