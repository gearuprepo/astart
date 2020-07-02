import heapq
import math
from helpers import Map, load_map, show_map

def shortest_path(Map,start,goal):
    #The buffer that holds the priority Queue results.
    buffer = [(0,start)]
    # Dict holding the cumulative cost of various nodes.
    node_costs = {}
    node_costs[start] = 0
    # Core route DS that is developed during the navigation of all routes
    base_route = {}
    base_route[start] = 0

    while len(buffer)>0:
        # min distance node from the priority queue to be popped up
        currNode = heapq.heappop(buffer)[1]
        nexts = Map.roads[currNode]
        if currNode == goal:
            break
        for nextnode in nexts:
            #calculate the cost interms of distance.
            localcost = distance(Map.intersections[currNode],Map.intersections[nextnode])
            cost = localcost + node_costs[currNode]
            if nextnode not in node_costs or cost<node_costs[nextnode]:
                base_route[nextnode] = currNode
                node_costs[nextnode] = cost
                heapq.heappush(buffer,(cost,nextnode)) 
    return traceroute(base_route,start,goal)

#Trace the complete route from the goal using reverse tracking mechanism.
def traceroute(path, start, goal):
    #Exception in case the goal is not found in the input path
    if goal not in path:
        return "Goal not found"
    node = goal
    retpath = []
    while node!=start:
        retpath.append(node)
        node = path[node]
    retpath.append(start)
    retpath.reverse()
    return retpath

# Find Euclidean distance 
def distance(start, end):
        return (math.hypot(end[0] - start[0], end[1] - start[1]))

#TC1
map_40 = load_map('map-40.pickle')
print(shortest_path(map_40, 5, 34))
# # (5, 34, [5, 16, 37, 12, 34]),
#TC2
map_10 = load_map('map-10.pickle')
print(shortest_path(map_10, 8, 10))
# # Not Found
#TC3
print(shortest_path(map_10, 0,2))
# 0,5,3,2