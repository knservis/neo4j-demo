# Neo4j REST demo

This is a demo of how to create a REST interface for querying [neo4j][neo4j].

Only one type of query will be supported, that is the shortest path between any two nodes, which in [Cypher][cypher] would look like this:

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
pip -r requirements.txt
```

### Configure the app to connect to neo4j

For instance if your neo4j instance is running on `http://192.168.99.100:7474` you should add the following to the config:

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

### Querying the server

Since there is only one endpoint in this demo, querying the server for the shortest path between to nodes is as simple as:

```bash
curl -D - http://127.0.0.1:5000/shortest_path/Entity/59032891/Entity/59029312
```

where 'Entity' is the node type and '59032891' and '59029312' are the node ids.

The query will return a JSON doc with three sections:

* Nodes ('nodes')
* Path ('path')
* Path abbreviated ('path_abbrev')

The Path and Path abbreviated contain a list of the edges of the first shortest path from node '59032891' to node '59029312'.

The difference between the two is that the 'abbreviated' version is easier read, but contains only edge information.

The Nodes list simply contains the nodes along the shortest path.

### Putting it all together

The easiest way to try out the whole project is to run it in docker with (from the project directory):

```bash

> docker run -it -p 5000:5000 -v $PWD:/app python:2.7 /bin/bash

> cd /app

> pip install -r requirements.txt

> export FLASK_APP=shortest_path_app

> export FLASK_ENV=development

> flask run --host=0.0.0.0

```

[neo4j]: https://neo4j.com/
[cypher]: https://neo4j.com/docs/cypher-refcard/current/
[py2neo]: http://py2neo.org/v4/
[flask]: http://flask.pocoo.org/docs/1.0/
