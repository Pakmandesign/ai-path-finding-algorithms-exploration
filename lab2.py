# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True 

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.
from graphs import GRAPH2
from graphs import GRAPH4


def bfs(graph, start, goal):
    # raise NotImplementedError
    agenda = [[start]]
    # for breath search the agenda is a queue
    visited = {}
    visited[start] = True
    # print(agenda)
    # print(visited)
    while agenda:
        path = agenda.pop(0)
        # print(path)
        node = path[-1]
        # get the element in the last position of the path
        # print(node)
        if node == goal:
            # print("----path----")
            # print(path)
            return path
        for neighbor in graph.get_connected_nodes(node):
            if neighbor not in visited:
                # print("----start neighbor---")
                # print(neighbor)
                visited[neighbor] = True
                # print("----visited----")
                # print(visited)
                agenda.append(path + [neighbor])
                # print("----agenda----")
                # print(agenda)
                # print("#####################")
                # break

# bfs(GRAPH4, 'S', 'G')
# path = ["S"]
# print(path[-1])


## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    agenda = [[start]]
    # for breath search the agenda is a stack FIFO because you want to keep exploring the last node you visited
    visited = {}
    visited[start] = True
    # print(agenda)
    # print(visited)
    while agenda:
        path = agenda.pop(0)
        # print(path)
        node = path[-1]
        # get the element in the last position of the path
        # print(node)
        if node == goal:
            # print("----path----")
            # print(path)
            return path
        for neighbor in graph.get_connected_nodes(node):
            if neighbor not in visited:
                # print("----start neighbor---")
                # print(neighbor)
                visited[neighbor] = True
                # print("----visited----")
                # print(visited)
                agenda.insert(0, path + [neighbor])


## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
# def find_best_heuristic(graph, node, goal):
def hill_climbing(graph, start, goal):
    agenda = [[start]]
    # for breath search the agenda is a stack FIFO because you want to keep exploring the last node you visited
    visited = {}
    visited[start] = True
    # print(agenda)
    # print(visited)
    while agenda:
        path = agenda.pop(0)
        # print(path)
        node = path[-1]
        # get the element in the last position of the path
        # print(node)
        if node == goal:
            # print("----path----")
            # print(path)
            return path
        for neighbor in graph.get_connected_nodes(node):
            if neighbor not in visited:
                # print("----start neighbor---")
                # print(neighbor)
                visited[neighbor] = True
                # print("----visited----")
                # print(visited)

                agenda.sort(key=lambda x: graph.get_heuristic(x[-1], goal))
                agenda.insert(0, path + [neighbor])

                print("----sorted----")
                print(agenda)

                # print("----agenda----")
                # print(agenda)


hill_climbing(GRAPH2, 'S', 'G')

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
