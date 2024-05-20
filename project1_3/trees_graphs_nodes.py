from coding import Stack, FIFO
class Tree:
    #Intializes the starting root node of the tree 
    def __init__(self, val):  
        #data of the node
        self.val = val
        #pointer to right child
        self.right = None
        #pointer to left child
        self.left = None
        
    def insert(self, val):
        #checks if the rootnode has been intialized and the initial root value is there
        if self.val:
            #follows the principle of a binary tree where values lower than the root value are to the left
            if self.val > val:
                #checks if the left child already has a value, if it doesn't then this is where the inserted value goes
                if self.left is None:
                    self.left = Tree(val)
                    
                #if the left child does have a value already in it, then do the insert search process again using the left child as the rootnode
                else:
                    self.left.insert(val)
            #follows the principle of a binary tree where values higher than the root value are to the right
            elif self.val < val:
                #checks if the right child already has a value, if it doesn't then this is where the inserted value goes
                if self.right is None:
                    self.right = Tree(val)
                   
                #if the right child does have a value already in it, then do the insert search process again using th6
                # e right child as the rootnode
                else:
                    self.right.insert(val)
            elif self.val == val:
                return False
    def inserts(self, l):
        if l.__class__ == list:
            for i in l:
                self.insert(i)
            return True
        elif isinstance(l, int):
            self.insert(l)
            return True
        
def traverse(tree, ds):
    #BFS
    if isinstance(tree, Tree) and isinstance(ds, FIFO):
        ds.insert(tree)
        q = []
        #runs the function while the loop is full
        while not ds.size() == 0:
            #retrieves the information of what node should the traversal go to next from the queue
                node = ds.get()
                q.append(node.val)
                #checks if the pointers are empty and if they aren't, stores their data in the queue
                if node.left is not None:
                    ds.insert(node.left)
                if node.right is not None:
                    ds.insert(node.right)
        return q
    #DFS
    elif isinstance(tree, Tree) and isinstance(ds, Stack):
        ds.push(tree)
        s = []
        #runs the function while the loop is full
        while not ds.size() == 0:
                #retrieves the information of what node should the traversal go to next from the stack
                node = ds.pop()
                s.append(node.val)
                #checks if the pointers are empty and if they aren't, stores their data in the stack
                if node.right is not None:
                    ds.push(node.right)
                if node.left is not None:
                    ds.push(node.left)
                
        return s
    
class Graph:
        def __init__(self, nodes_list):
            self.graph = []
            self.nodes = nodes_list
        
        def add_edge(self, n1, n2, weight):
            self.graph.append([n1,n2,weight])
        
        def add_node(self, node):
            self.nodes.append(node)
        
        def return_graph(self):
            return self.graph
        
        def return_nodes(self):
            return len(self.nodes)
        
        #multiple edge adding for convenience
        def add_edges(self, edge_list):
            if isinstance(edge_list, list):
                for edge in edge_list:
                    self.graph.append(edge)
                  
            
        #
        def helper_find(self, parent, index):
            if parent[index] == index:
                return index
            return self.helper_find(parent, parent[index])
        
        def union_helper(self, parent, rank, x, y):
            xroot = self.helper_find(parent, x)
            yroot = self.helper_find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1
        def debug(self):
            return len(self.nodes)
        
        def kruskal(self):
            
            self.nodes = list(set(self.nodes))
            ans = []
            index = 0 
            edge_index = 0
            parent = []
            rank = []
          
            graph = self.graph
            self.graph = sorted(self.graph, key=lambda item: item[2])
            
            for i in range((len(self.nodes))):
                parent.append(i)
                rank.append(0)
        
            while edge_index < (len(self.nodes)) - 1:
                #pulls the edge info out of the graph
                n1, n2, weight = graph[index]
                index += 1 
                x = self.helper_find(parent, n1-1)
                y = self.helper_find(parent, n2-1)
                 
                if x != y:
                    edge_index += 1
                    ans.append((n1,n2,weight))
                    self.union_helper(parent, rank, x, y)
            total_weight = 0
            for i in range(len(ans)):
                total_weight += ans[i][2]
            return f'MST:{ans}', f'Total MST weight:{total_weight}'
        
        def djikstra(self, source):
            #where the resulting shortest paths will be stored
            dist = {node:float('inf') for node in self.nodes}
            #the distance from source -> source is always 0
            dist[source] = 0
            unvisited = set(self.nodes)
            
            while unvisited:
                #retrieves the lowest node in the unvisited set
                curr_node = min(unvisited, key=lambda node: dist[node])
                unvisited.remove(curr_node)
                
                #for loop which checks if each edge connected to the current node has a lower weight than the current lowest weight path the algorithm has in the dist dictionary
                for neighbor, weight in self.neighbors(curr_node):
                    new_dist = dist[curr_node] + weight
                    #if it does have a lower weight then update the lowest weight path in the dictionary
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        unvisited.add(neighbor)
                
            return dist
        
        def neighbors(self, node):
            neighbors = []
            #retrieves the edge that connects the source
            for edge in self.graph:
                if edge[0] == node:
                    neighbors.append([edge[1], edge[2]])
                elif edge[1] == node:
                    neighbors.append([edge[0], edge[2]])
            #attempted patch to the algorithm to make it work for paths with multiple edges, but it just increases the amount of edges to a path by 1 instead
            for edge1 in self.graph:
                if edge1[0] == node:
                    for edge2 in self.graph:
                        if edge1[1] == edge2[0] and edge1[1] != edge2[1]:
                            neighbors.append((edge2[1], edge1[2] + edge2[2]))   
            return neighbors          
