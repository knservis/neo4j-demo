from shortest_path_app import create_app

def test_config():
    assert not create_app().testing
    db_url = 'http://192.168.99.100:7474'
    assert create_app({'TESTING': True, 'DATABASE': db_url}).testing

def test_index(client):
    response = client.get('/')
    assert response.data == b'Rest Shortest path demo app'


def test_shortest_path(client):
    expected_response = '''[{"valid_until": "Malta corporate registry data is current through 2016", "status": "", "closed_date": "", "ibcRUC": "C 39144", "name": "SKILL GAMES NETWORK LIMITED", "countries": "", "sourceID": "Paradise Papers - Malta corporate registry", "jurisdiction": "MLT", "company_type": "", "note": "", "node_id": "59032891", "address": "", "jurisdiction_description": "Malta", "incorporation_date": "Jul 14, 2006", "country_codes": "", "type": "", "service_provider": ""}, {}, {"valid_until": "Malta corporate registry data is current through 2016", "status": "", "closed_date": "", "ibcRUC": "", "name": "SG HOLDINGS LIMITED", "countries": "", "sourceID": "Paradise Papers - Malta corporate registry", "jurisdiction": "", "company_type": "", "note": "", "node_id": "59155606", "address": "", "jurisdiction_description": "", "incorporation_date": "", "country_codes": "", "type": "", "service_provider": ""}, {}, {"valid_until": "Malta corporate registry data is current through 2016", "status": "", "closed_date": "", "ibcRUC": "C 35527", "name": "SKILL GAMES LIMITED", "countries": "", "sourceID": "Paradise Papers - Malta corporate registry", "jurisdiction": "MLT", "company_type": "", "note": "", "node_id": "59029312", "address": "", "jurisdiction_description": "Malta", "incorporation_date": "Jan 25, 2005", "country_codes": "", "type": "", "service_provider": ""}]''' 
    response = client.get('/shortest_path/Entity/59032891/Entity/59029312')
    print response
    assert response.data == expected_response
