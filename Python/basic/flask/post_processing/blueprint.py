from flask import Blueprint, request, current_app as app
from time import sleep

bp = Blueprint('app', __name__)


@bp.route('/')
def root():
    body = request.json

    @app.after_response
    def worker():
        print(body)
        sleep(5)
        print('finished_after_processing')

    print('returned')
    return 'finished_fast', 200
