# Neo4j REST demo

This is a demo of how to create a REST interface for querying [neo4j][neo4j]. 

Only one type of query will be supported, that is the shortest path between any two nodes, whicn in [Cypher][cypher] would look like this: 
```
MATCH (a:<label-a>{node_id: "<node-id-1>"}),(b:<label-b>{node_id: "<node-id-2>"}), p = shortestPath((a)-[*]-(b)) RETURN p;
```

The `python` language and [driver][driver] will be used.



[neo4j]: https://neo4j.com/
[swagger]: https://swagger.io/
[cypher]: https://neo4j.com/docs/cypher-refcard/current/
[driver]: https://neo4j.com/developer/python/