import pytest
import json
from mock import patch, MagicMock, PropertyMock, DEFAULT
from shortest_path_app import create_app

def test_config():
    assert not create_app().testing
    db_url = 'http://192.168.99.100:7474'
    assert create_app({'TESTING': True, 'DATABASE': db_url}).testing

def test_index(client):
    with patch('shortest_path_app.db.Graph') as db_patch:
        db_patch.return_value = None
        response = client.get('/')
        assert response.data == b'REST Shortest path demo app'

def test_shortest_path(client):
    expected_response = {}
    expected_response_json = json.dumps(expected_response) + "\n"
    with patch('shortest_path_app.db.Graph') as db_patch:
        mock_db = MagicMock()
        mock_db.node_labels = ['Entity']
        mock_db.evaluate.return_value = expected_response
        db_patch.return_value = mock_db
        response = client.get('/shortest_path/Entity/59032891/Entity/59029312')
        assert response.data == expected_response_json

def test_shortest_path_invalid_label(client):
    with patch('shortest_path_app.db.Graph') as db_patch:
        mock_db = MagicMock()
        mock_db.node_labels = ['Entity']
        db_patch.return_value = mock_db
        patch.return_value = None
        with pytest.raises(ValueError) as e:
            _ = client.get('/shortest_path/Jim/59032891/Entity/59029312')
        assert 'Jim label not in the graph!' in e.value

def test_shortest_path_invalid_node_id(client):
    with patch('shortest_path_app.db.Graph') as db_patch:
        db_patch.return_value = None
        response = client.get('/shortest_path/Entity/Entity/Entity/59029312')
        assert response.status == '404 NOT FOUND'

