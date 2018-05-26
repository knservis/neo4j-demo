import os
import json
from flask import Flask, Response
from shortest_path_app.db import get_db

def create_app(test_config=None):
    '''
    Demo REST application that only serves one path, namely:
    /shortest_path/[parameter_list]

    Example: /shortest_path/Entity/59032891/Entity/59029312

    Some basic TODOs (In case this is used as an example to a real application):
    - Request parameter sanitise/escape for cql.
    - Static assets.
    - Decouple request from response, using a queue and redirecting to result and/or using flash().
    - Use a proper key.
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'))
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'Rest Shortest path demo app'

    @app.route(
        '/shortest_path/<string:label_a>/<int:node_id_a>/<string:label_b>/<int:node_id_b>'
    )
    def shortest_path(label_a, node_id_a, label_b, node_id_b):
        db = get_db()
        ret = json.dumps(db.get_shortest_path_relationship(label_a, node_id_a, label_b, node_id_b))
        resp = Response(response=ret,
                    status=200,
                    mimetype='application/json')
        return resp

    return app