# https://stackoverflow.com/questions/48994440/execute-a-function-after-flask-returns-response/60663373#60663373

from flask import Flask
from .blueprint import bp
from .library import AfterResponse

app = Flask(__name__)

with app.app_context():
    app.register_blueprint(bp, url_prefix='/')
    AfterResponse(app)
