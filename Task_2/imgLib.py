import cv2
import numpy as np

# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)
# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
def detectCellVal(img_rgb,grid_map):
       
        img0= cv2.imread('digits\\0.jpg')
        img_0=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
        img1= cv2.imread('digits\\1.jpg')

        img_1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        threshold=0.6
        col_start=0
        col_end=50
        for i in range(0,14):
           row_start=0
           row_end=50
           for j in range(0,14):    
                  template=img_rgb[col_start:col_end,row_start:row_end]      ##croping a specific part of image(a sub-square of 50*50 pixel) and making it the template
                  
                   ## NOW MATCING THE CROPED TEMPLATE, ONE BY ONE , WITH EACH DIGIT 
                  threshold=0.4
                  res=cv2.matchTemplate(img_1,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:  ## match is found
                      grid_map[i][j]=1
                      
                  threshold=0.6
                  res=cv2.matchTemplate(img_0,template,cv2.TM_CCOEFF_NORMED)
                  min_value,max_value,min_loc,max_loc=cv2.minMaxLoc(res)
                  if max_value>=threshold:## match is found
                         grid_map[i][j]=0

                  row_start=row_start+50
                  row_end=row_end+50
                  
           col_end=col_end+50
           col_start=col_start+50
        return grid_map 
############################################################################################
# solveGrid finds the shortest path,
# between valid grid cell in the start row 
# and valid grid cell in the destination row 
# solveGrid(grid_map)
# Return the route_path and route_length

class Graph(object): ## a class of graph having methods in it to form the reqired weighted(1 ) graph
   
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)
    
    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)   ## since it is an undirected graph hence joining the edge towards each of the node
        self._add_edge(to_node, from_node, distance)
 
    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)               ## adding edge with distance from given node to destination node
        self.distances[(from_node, to_node)] = distance
 
### dijistras method to compute the shortest path between two nodes in an undirected graph 
def dijkstra(graph, initial_node):
    visited = {initial_node: 0}  ##distance of intial node from itself is zero
    current_node = initial_node
    path = {}  
    
    nodes = set(graph.nodes)  
    
    while nodes: ## dequeueing  a neighbourhood node (minimum)
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
 
        if min_node is None: ## if there is nothing in the neighbourhood then break
            break
 
        nodes.remove(min_node)
        cur_wt = visited[min_node]
        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]: ## updating the adjacent node's distance if effective weight from source is minimum from previous value
                visited[edge] = wt
                path[edge] = min_node
    
    return visited, path ##returning the  visited list (which contains all the path from source to all other reachable position) and the path
 
def shortest_path(graph, initial_node, goal_node):
    distances, paths = dijkstra(graph, initial_node)
    if goal_node not in distances: ## if goal_node is not in the list of all the reachable position from the source then break immediedtly
            return -1
    route = [goal_node]
 ## performing the dijistras algorithm
    while goal_node != initial_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node] 

    route.reverse() ## reversing the list to get the list which starts from the source and end to the destination
    return route

## the below method checks wheather the given row and col. are in bound or not
def isValid(row,col):
        if row>=0 and row<14 and col>=0 and col<14:
                return 1
        else:
                return 0       
 
def solveGrid(grid_map):

                route_length=0
                route_path=[]
                ##your code here
                x_ref= [-1, 0, 0, 1,1,-1,-1,1]  ## these two list are made to iterate left,right,digonally as prescribed
                y_ref= [0, -1, 1, 0,1,-1,1,-1]       
                g=Graph()  ##intializing the instance of the graph class

                for i in range(0,14):  
                    for j in range(0,14):          ## adding the nodes to the graph (only if it is valid i.e grid_map[i][j]==1)
                        if grid_map[i][j] is 1:
                            g.add_node(14*i+j)

                ## the below snippet adds the edge from one node to another    
                for i in range(0,14):
                    for j in range(0,14):
                        if grid_map[i][j] is 1:
                            for k in range(0,8):   ## this to iterate left,rightand digonally and chacking wheather there is actually a path or not .If the path is there then weight of that path will be 1   
                                temp_i=i+x_ref[k]
                                temp_j=j+y_ref[k]
                                if isValid(temp_i,temp_j) is 1 and grid_map[temp_i][temp_j] is 1: ## also checking wheather the iterated indeces are in range
                                    g.add_edge(14*i+j , 14*temp_i+temp_j , 1)

                x=9999 ##defining a temprory varible having infinte path length
                for i in range(0,14):
                   if grid_map[0][i] is 0:
                       continue                  ## continuing if there is not actually a valid edge
                   for j in range(0,14):
                       if grid_map[13][j] is 0 :
                         continue

                       ## now these three elif statements check wheather all the surrounding elements are zero or not. If all the surrounding elements are zero then
                        ## we dont proceed to the dijistras algorithm because if we proceed with this condition then error will be detected in that  method.we have 
                        ## ignored this corner case in dijistras method and hence we take care of that here only
                        
                       elif i is 0 and grid_map[0][i+1] is 0 and grid_map[1][i] is 0 and grid_map[1][i+1] is 0: 
                                continue
                       elif i is 13 and grid_map[0][i-1] is 0 and grid_map[1][i] is 0 and grid_map[1][i-1] is 0:
                                continue
                       elif i >0 and i<13 and grid_map[0][i+1] is 0 and grid_map[0][i-1] is 0 and grid_map[1][i] is 0 and grid_map[1][i+1] is 0 and  grid_map[1][i-1] is 0:
                                continue

                       ##if everthing is fine then we proceed to dijistras method
                        
                       short_path=shortest_path(g,i,182+j)
                       if short_path is -1:
                               continue
                       if len(short_path)<x:               ## setting up the shortest path by comparing it with available shortest in each iteration
                               route_path=short_path
                               x=len(short_path)
                                            
                if x is 9999: ## if x is not change that means there is no path there from source to destination
                        return route_path,0
                else:
                        return route_path,x-1  ##else return the route path and route length

## this method is there to show the shortest path in graph by drawing the blue line
                
def drawPath(grid_map,path):
        if len(path) is 0:
                  return grid_map        
        grid_map=cv2.cvtColor(grid_map,cv2.COLOR_GRAY2BGR)
        for i in range(0,len(path)-1):
                x_1=path[i]%14
                y_1=path[i]//14
                x_2=path[i+1]%14
                y_2=path[i+1]//14
                cv2.line(grid_map,(25+50*x_1,25+50*y_1),(25+50*x_2,25+50*y_2),(255,0,0),4)
        return grid_map        
############################################################################################     
