import pytest
from shortest_path_app.db import get_db

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

        db.execute('MATCH (n: Entity{node_id:"59032891"}) RETURN n')

    assert None == db.execute('MATCH (n: Entity{node_id:"59032891"}) RETURN n')
