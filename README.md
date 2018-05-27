# Neo4j REST demo

This is a demo of how to create a REST interface for querying [neo4j][neo4j].

Only one type of query will be supported, that is the shortest path between any two nodes, whicn in [Cypher][cypher] would look like this:

```cql
MATCH (a:<label-a>{node_id: "<node-id-1>"}),(b:<label-b>{node_id: "<node-id-2>"}), p = shortestPath((a)-[*]-(b)) RETURN p;
```
The `python` language and [py2neo][py2neo] will be used.

The REST interface is created using [Flask][flask].

## Run

To run this you will need to:
### Have all the required libraries installed

You can install the required libraries using:
```bash
pip -r reuirements.txt
```

### Configure the app to connect to neo4j

For instance if your neo4j instance is running on `http://192.168.99.100:7474` you should add the floowing to the config: 
```python
DATABASE = 'http://192.168.99.100:7474'
```
in the configuration file in `instance/config.py`

### Start server

Finally you can start the server with:
```bash
export FLASK_APP=shortest_path_app
export FLASK_ENV=development
flask run
```


[neo4j]: https://neo4j.com/
[cypher]: https://neo4j.com/docs/cypher-refcard/current/
[py2neo]: http://py2neo.org/v4/
[flask]: http://flask.pocoo.org/docs/1.0/
