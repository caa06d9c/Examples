from flask import Flask
from .blueprint import bp
from .library import AfterResponse

app = Flask(__name__)

with app.app_context():
    app.register_blueprint(bp, url_prefix='/')
    AfterResponse(app)



