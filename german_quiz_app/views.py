
import flask
from application import app
from datetime import datetime as dt


@app.route('/')
def hello_world():
    message = "Hello, world!"
    return flask.render_template('index.html',
                                  title=message,
                                  date_today=dt.now().strftime("%Y-%m-%d"),
                                  flask_debug=app.debug,
                                  app_version=app.config['APP_VERSION'],
                                  enable_cool_new_feature=app.config['enable_cool_new_feature'])