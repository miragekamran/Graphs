# UNDERSTANDING:


# Input data: a graph of realationships between parents and children over multiple generations.

# Data format: a list of (parent, child) pairs
# Each individual is assigned a unique integer id.

# Output data: return individual's earliest known ancestor
# the one at the furthest distance from the input individual.
# If there is more than one ancestor tied for "earliest",
# return the one with the lowest numeric ID.
# If the input individual has no parents, the function should return -1.

# PLAN AND EXECUTE:
from util import Queue
# using the Graph class from graph project we create the graph for this task
from graph import Graph


def earliest_ancestor(ancestors, starting_node):

    # Call the graph method and create a var for it
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    # Call the queue method and create a var for it
    queue = Queue()

    # Add the starting node to the queue
    queue.enqueue([starting_node])

    # Create a set to store the visited vertices
    visited = set()

    # Set the earliest ancestor to -1 if the input individual has no parents
    earliest_ancestor = -1
    # While queue is not empty
    while queue.size() > 0:
        # dequeue the current PATH from the queue
        path = queue.dequeue()
        # Create a var to get the last node in the path
        vertex = path[-1]

        # if vertex not visited:
        if vertex not in visited:
            visited.add(vertex)

            # Check if the vertex is less than the parent
            if ((vertex < earliest_ancestor) or (len(path) > 1)):
                # set the parent as the vertex
                earliest_ancestor = vertex

            # for neighbors of the current vertex
            for neighbor in graph.get_neighbors(vertex):
                new_path_copy = list(path)
                new_path_copy.append(neighbor)
                queue.enqueue(new_path_copy)
    

    return earliest_ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]



#   10
#   /
#  1 2  4  11
#  \/  /\ /
#  3  5  8
#  \ / \  \
#   6  7  9

print(f'the earliest ancestor for 1>> {earliest_ancestor(test_ancestors, 1)}')
print(f'the earliest ancestor for 2>> {earliest_ancestor(test_ancestors, 2)}')
print(f'the earliest ancestor for 3>> {earliest_ancestor(test_ancestors, 3)}')
print(f'the earliest ancestor for 4>> {earliest_ancestor(test_ancestors, 4)}')
print(f'the earliest ancestor for 5>> {earliest_ancestor(test_ancestors, 5)}')
print(f'the earliest ancestor for 6>> {earliest_ancestor(test_ancestors, 6)}')
print(f'the earliest ancestor for 7>> {earliest_ancestor(test_ancestors, 7)}')
print(f'the earliest ancestor for 8>> {earliest_ancestor(test_ancestors, 8)}')
print(f'the earliest ancestor for 9>> {earliest_ancestor(test_ancestors, 9)}')
print(f'the earliest ancestor for 10>> {earliest_ancestor(test_ancestors, 10)}')
print(f'the earliest ancestor for 11>> {earliest_ancestor(test_ancestors, 11)}')
