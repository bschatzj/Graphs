from graph import Graph
from util import Queue

# def earliest_ancestor(ancestors, starting_node, has_parent=False):
#     for parent, child in ancestors:
#         if child == starting_node:
#             return earliest_ancestor(ancestors, parent, True)

#     return starting_node if has_parent == True else -1






def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    # Load the Graph
    for ancestor in ancestors:
        g.add_node(ancestor[0])
        g.add_node(ancestor[1])
        g.add_edge(ancestor[1], ancestor[0])

    result = g.dfs(starting_node)
    max_value = 0
    new_result = None
    if result == -1:
        return result
    for data in result:
        if data[1] == max_value:
            if new_result is not None:
                if new_result[0] > data[0]:
                    new_result = data
            else:
                new_result = data
        elif data[1] > max_value:
            max_value = data[1]
            new_result = data

    return new_result[0]
