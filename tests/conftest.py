import os
import tempfile

import pytest
from shortest_path_app import create_app
from shortest_path_app.db import get_db

@pytest.fixture
def app():
    db_url = 'http://192.168.99.100:7474'

    app = create_app({
        'TESTING': True,
        'DATABASE': db_url,
    })

    # with app.app_context():
    #     # init_db()
    #     get_db().executescript(_data_sql)

    yield app

    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
