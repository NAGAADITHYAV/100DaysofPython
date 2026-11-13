from collections import deque
class Node:
    def __init__(self, data, edges = None):
        self.data = data
        self.edges = edges

class GraphCodec:
    def encode(self, start):
        # takes in a entry point to a graph and stores graph as a simple array
        '''
        [
          no.of_nodes,
          start_node_id,

          node_id, value, number_of_edges_that_start_from_nodeid, nodeids,
          node_id, value, number_of_edges_that_start_from_nodeid, nodeids
          node_id, value, number_of_edges_that_start_from_nodeid, nodeids
        ]
        '''
        if not start:
            return [0, -1]
        no_of_nodes = 1
        curr_id = 0
        graph = [no_of_nodes, curr_id]

        visited = set([start])
        
        q = deque([start])

        while(q):
            curr_node = q.popleft()
            neighbours = curr_node.edges
            
        
        
        
        return graph
        

    def decode(self, graph_encoded):
        #takes a single array and gives outlist of nodes
        pass

# Step 1: create nodes (no edges yet)
A = Node(1)
B = Node(2)
C = Node(14)
D = Node(41)
E = Node(4)

# Step 2: assign edges
A.edges = [B, E]
B.edges = [C]
C.edges = [D]
D.edges = [A]
E.edges = [C]

g = GraphCodec()

def print_graph_encoded(graph_encoded):
    pass

graph_encoded = g.encode(A)
print_graph_encoded(graph_encoded)
graph = g.decode(graph_encoded)



