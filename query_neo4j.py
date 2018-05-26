#!/usr/bin/env python

from py2neo import Graph, walk

class Neo4jClient(object):
    """ Client to neo4j database """

    graph = None

    def __init__(self, uri):
        self.graph = Graph(uri)

    def get_shortest_path_relationship(self, label_a, node_id_a, label_b, node_id_b):
        """Returns the first shortest path between two nodes identified by label and node_id 

        If there are any results (there could be many shortest paths), it returns the first one (as per spec).
        The path is returned as a list, from the start node, to the end node including the relationships in between.

        Keyword arguments:
        label_a -- The label for node A (e.g. 'Address')
        node_id_a -- The node_id for entity A (e.g. 5124536)
        label_b -- The label for node B (e.g. 'Entity')
        node_id_b -- The node_id for entity B (e.g. 5124537)
        """

        errors = [ '{s} label not in the graph!'.format(l) for l in [label_a, label_b] if not l in self.graph.node_labels]
        if errors:
            raise "\n".join(errors)
        query = """MATCH (a:{label_a}{{node_id: \"{node_id_a}\"}}),
            (b:{label_b}{{node_id: \"{node_id_b}\"}}),
            p = shortestPath((a)-[*]-(b)) RETURN p""".format(label_a=label_a, label_b=label_b, node_id_a=node_id_a, node_id_b=node_id_b)
        result = self.graph.evaluate(query)
        return [ i for i in walk(result)] if result else []


if __name__ == "__main__":
    nc = Neo4jClient("http://192.168.99.100:7474")
    print nc.get_shortest_path_relationship('Entity', "59032891", 'Entity', "59029312")
