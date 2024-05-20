from coding import Stack
from coding import FIFO
from coding import OQ
from trees_graphs_nodes import Tree, Graph, traverse
#Code Below is project 2 uptil the project 1 comment
class class_test_traversal:
    def __init__(self):
        
        self.t1 = Tree(10)
        self.t2 = Tree(10)
        self.fifo1 = FIFO(10)
        self.stack2 = Stack(10)
        self.return_value = True
        self.g4 = Graph([0,1,2,3,4,5,6])
    
    def test_BFS(self):
        #simple check to see if BFS works
        self.t1.inserts([5,15,3,7,12,19,1,2,8,11,13,17,22,5])
        if not traverse(self.t1,self.fifo1) == [10, 5, 15, 3, 7, 12, 19, 1, 8, 11, 13, 17, 22, 2]:
            print("Test 1 in test_traversal failed")
            self.return_value = False 
        pass
    

    def test_DFS(self):
        #simple check to see if DFS works
        self.t2.inserts([5,15,3,7,12,19,1,2,8,11,13,17,22])
        if not traverse(self.t2,self.stack2) == [10, 5, 3, 1, 2, 7, 8, 15, 12, 11, 13, 19, 17, 22]:
            print("Test 2 in test_traversal failed")
            self.return_value = False 
            
    def return_bool(self):
        return self.return_value

class class_test_kruskal:
    def __init__(self):
        
        self.g1 = Graph([1,2,3,4,2,5,6,6,7,8,9])
        self.g2 = Graph([1,2,3,4,5,6])
        self.g3 = Graph([1,2,3,4,2,5,6,6,7,8,9,4,3,2,1])
        self.return_value = True

    def classic_test(self):
        #checks to see if the kruskal alg returns the right MST
        self.g2 = Graph([1,2,3,4,5,6])
        self.g2.add_edge(0, 1, 4)
        self.g2.add_edge(0, 1, 4)
        self.g2.add_edge(0, 2, 4)
        self.g2.add_edge(0, 2, 4)
        self.g2.add_edge(0, 2, 4)
        self.g2.add_edge(1, 2, 2)
        self.g2.add_edge(1, 0, 4)
        self.g2.add_edge(2, 0, 4)
        self.g2.add_edge(2, 1, 2)
        self.g2.add_edge(2, 3, 3)
        self.g2.add_edge(2, 5, 2)
        self.g2.add_edge(2, 4, 4)
        self.g2.add_edge(3, 2, 3)
        self.g2.add_edge(3, 4, 3)
        self.g2.add_edge(4, 2, 4)
        self.g2.add_edge(4, 3, 3)
        self.g2.add_edge(5, 2, 2)
        self.g2.add_edge(5, 4, 3)        
        if not self.g2.kruskal() == ('MST:[(0, 1, 4), (0, 2, 4), (2, 3, 3), (2, 5, 2), (2, 4, 4)]', 'Total MST weight:17'):
            print("Test 1 in test_kruskal failed")
            self.return_value = False 
    def duplicate_nodes_and_edges(self):
        #checks to see if the kruskal alg can properly return the right MST with duplicate edges and nodes added
        self.g1 = Graph([1,2,3,4,2,5,6,6,7,8,9])
        self.g1.add_edge(1,2,4)
        self.g1.add_edge(1,2,4)
        self.g1.add_edge(1,3,8)
        self.g1.add_edge(2,3,11)
        self.g1.add_edge(2,4,8)
        self.g1.add_edge(3,5,7)
        self.g1.add_edge(3,6,1)
        self.g1.add_edge(4,5,2)
        self.g1.add_edge(5,6,6)
        self.g1.add_edge(6,7,2)
        self.g1.add_edge(4,7,4)
        self.g1.add_edge(4,8,7)
        self.g1.add_edge(5,6,6)
        self.g1.add_edge(8,7,14)
        self.g1.add_edge(8,9,9)
        self.g1.add_edge(7,9,10)
        if not self.g1.kruskal() == ('MST:[(1, 2, 4), (1, 3, 8), (2, 4, 8), (3, 5, 7), (3, 6, 1), (6, 7, 2), (4, 8, 7), (8, 9, 9)]', 'Total MST weight:46'):
            print("Test 2 in test_kruskal failed")
            self.return_value = False 
    def multi_edge_add(self):
        #checks to see if add_edges works as intended with duplicates
        self.g3 = Graph([1,2,3,4,2,5,6,6,7,8,9,4,3,2,1])
        self.g3.add_edges([[2, 3, 11],[9,4,8],[1,2,4],[1,3,8], [2, 3, 11],[2,4, 8], [3,5,7],[3,6,1],[4,5,2],[5,6,6],[6,7,2],[4,7,4],[4,8, 7],[8, 7, 14],[8, 9, 9],[7,9, 10]])
        if not self.g3.kruskal() == ('MST:[(2, 3, 11), (9, 4, 8), (1, 2, 4), (2, 4, 8), (3, 5, 7), (3, 6, 1), (6, 7, 2), (4, 8, 7)]', 'Total MST weight:48'):
            print("Test 3 in test_kruskal failed")
            self.return_value = False 
    def return_bool(self):
        return self.return_value
    
class class_test_djikstra:
    def __init__(self):
        self.g4 = Graph([0,1,2,3,4,5])
        self.g5 = Graph([1,2,3,4,5,6,7,8,9])
        self.return_value = True
    
    def classic_test(self): 
        #checks if the graph correctly returns the shortest path from each node to the selected node   
        self.g4 = Graph([0,1,2,3,4,5])
        self.g4.add_edge(0, 1, 4)
        self.g4.add_edge(0, 1, 4)
        self.g4.add_edge(0, 2, 4)
        self.g4.add_edge(0, 2, 4)
        self.g4.add_edge(0, 2, 4)
        self.g4.add_edge(1, 2, 2)
        self.g4.add_edge(1, 0, 4)
        self.g4.add_edge(2, 0, 4)
        self.g4.add_edge(2, 1, 2)
        self.g4.add_edge(2, 3, 3)
        self.g4.add_edge(2, 5, 2)
        self.g4.add_edge(2, 4, 4)
        self.g4.add_edge(3, 2, 3)
        self.g4.add_edge(3, 4, 3)
        self.g4.add_edge(4, 2, 4)
        self.g4.add_edge(4, 3, 3)
        self.g4.add_edge(5, 2, 2)
        self.g4.add_edge(5, 4, 3)
        if not self.g4.djikstra(0) == {0: 0, 1: 4, 2: 4, 3: 7, 4: 8, 5: 6}:
            print("Test 1 in test_djiikstra failed")
            self.return_value = False
    def multi_edge_paths(self):
        #checks if the graph will work for cases where the shortest path has multiple edges
        self.g5 = Graph([1,2,3,4,5,6,7,8,9])
        self.g5.add_edges([[2, 3, 11],[9,4,8],[1,2,4],[1,3,8], [2, 3, 11],[2,4, 8], [3,5,7],[3,6,1],[4,5,2],[5,6,6],[6,7,2],[4,7,4],[4,8, 7],[8, 7, 14],[8, 9, 9],[7,9, 10]])
        if not self.g5.djikstra(2) == {1: 4, 2: 0, 3: 11, 4: 8, 5: 10, 6: 12, 7: 12, 8: 15, 9: 22}:
            print("Test 2 in test_djiikstra failed")
            self.return_value = False
    
    def return_bool(self):
        return self.return_value
        
def test_kruskal():
    k = class_test_kruskal()
    k.classic_test()
    k.duplicate_nodes_and_edges()
    k.multi_edge_add()
    return(k.return_bool())

def test_traverse():
    t = class_test_traversal()
    t.test_BFS()
    t.test_DFS()
    return(t.return_bool())

def test_djikstra():
    d = class_test_djikstra()
    d.classic_test()
    d.multi_edge_paths()
    return(d.return_bool())

def test_project2():
    print(test_kruskal())
    print(test_traverse())
    print(test_djikstra())

test_project2()









#Code below is Project 1   
class class_test_stack:
    def __init__(self):
        self.s1 = Stack(5)
        self.s2 = Stack(7)
        self.s3 = Stack(10)
        self.s4 = Stack(10)
        self.return_value = True
    def test_pop(self):
        self.s1.push(1)
        self.s1.push(2)
        #Test 1
        #simple test to see if pop is returning the last value put in
        if not self.s1.pop() == 2:
            print("Test 1 in test_stack failed")
            self.return_value = False  
        self.s1.push(3)
        self.s1.push(4)
        self.s1.push(5)
        #Test 2
        #simple test to see if pop is returning the last value put in
        if not self.s1.pop() == 5:
            print("Test 2 in test_stack failed")
            self.return_value = False  
        self.s1.push(4)
        self.s1.push(5)
    def test_push(self):
        #Test 3
        #checks if push realizes the stack is full
        if not self.s1.push(20) == False:
            print("Test 3 in test_stack failed")
            self.return_value = False 
        self.s1.pop()
        self.s1.push("hi")
        #Test 4
        #checks if push can take strings
        if not self.s1.pop() == "hi":
            print("Test 4 in test_stack failed")
            self.return_value = False 
    def pops(self):
        self.s2.push(1)
        self.s2.push(2)
        self.s2.push(3)
        self.s2.push(4)
        self.s2.push(5)
        self.s2.push(6)
        self.s2.push(7)
        #Test 5      
        #checks if pops works as intended  
        if not self.s2.pops(7) == [7,6,5,4,3,2,1]:
            print("Test 5 in test_stack failed")
            self.return_value = False 
        #Test 6
        #checks if pops returns en empty list when used on an empty stack
        if not self.s2.pops(5) == []:
            print("Test 6 in test_stack failed")
            self.return_value = False 
    def property_testing(self):
        self.s3.push(1)
        self.s3.push(2)
        self.s3.push(10)
        for i in (range(10)):
            self.s4.push(i+1)
        if not self.s3.pop() == self.s4.pop():
            print("Test 7 in test_stack failed")
            self.return_value = False
        
    def return_bool(self):
        return self.return_value

class class_test_queue:
    def __init__(self):
        self.s1 = FIFO(5)
        self.s2 = FIFO(7)
        self.s3 = FIFO(10)
        self.s4 = FIFO(10)
        self.return_value = True
    def test_insert(self):
        self.s1.insert(1)
        self.s1.insert(2)
        #Test 1
        #simple test to see if get is returning the first value put in
        if not self.s1.get() == 1:
            print("Test 1 in test_queue failed")
            self.return_value = False  
        self.s1.insert(3)
        self.s1.insert(4)
        self.s1.insert(5)
        #Test 2
        #simple test to see if get is returning the first value put in
        if not self.s1.get() == 2:
            print("Test 2 in test_queue failed")
            self.return_value = False  
        self.s1.insert("hi")
        self.s1.insert(4)
        self.s1.insert(5)
    def test_get(self):
        #Test 3
        #checks if insert realizes the queue is full
        if not self.s1.insert(20) == False:
            print("Test 3 in test_queue failed")
            self.return_value = False 
        self.s1.get()
        self.s1.get()
        self.s1.get()
        #Test 4
        #checks if insert can take strings
        if not self.s1.get() == "hi":
            print("Test 4 in test_queue failed")
            self.return_value = False 
    def test_gets(self):
        self.s2.insert(1)
        self.s2.insert(2)
        self.s2.insert(3)
        self.s2.insert(4)
        self.s2.insert(5)
        self.s2.insert(6)
        self.s2.insert(7)
        #Test 5      
        #checks if gets works as intended  
        if not self.s2.gets(7) == [1,2,3,4,5,6,7]:
            print("Test 5 in test_queue failed")
            self.return_value = False 
        #Test 6
        #checks if gets returns en empty list when used on an empty queue
        if not self.s2.gets(5) == []:
            print("Test 6 in test_queue failed")
            self.return_value = False 
    def property_testing(self):
        self.s3.insert(1)
        self.s3.insert(2)
        self.s3.insert(10)
        for i in (range(10)):
            self.s4.insert(i+1)
        if not self.s3.get() == self.s4.get():
            print("Test 7 in test_queue failed")
            self.return_value = False
    def return_bool(self):
        return self.return_value
    
class class_test_oq:
    def __init__(self):
        self.s1 = OQ(10)
        self.s2 = OQ(10)
        self.s3 = OQ(10)
        self.s4 = OQ(10)
        self.return_value = True
        
    #Test 1
    #Tests if the OQ successfully orders the list
    def property_testing(self):
        self.s3.insert(1)
        self.s3.insert(2)
        self.s3.insert(10)
        self.s3.insert(3)
        self.s3.insert(5)
        self.s3.insert(7)
        self.s3.insert(6)
        self.s3.insert(9)
        self.s3.insert(8)
        self.s3.insert(4)
        for i in (range(10)):
            self.s4.insert(i+1)
        if not self.s3.gets(10) == self.s4.gets(10):
            print("Test 1 in test_oq failed")
            self.return_value = False
            
    def return_bool(self):
        return self.return_value
    
def test_stack():
    s = class_test_stack()
    s.test_pop()
    s.test_push()
    s.pops()
    s.property_testing()
    return s.return_bool()

def test_queue():
    q = class_test_queue()
    q.test_insert()
    q.test_get()
    q.test_gets()
    q.property_testing()
    return q.return_bool()

def test_oq():
    oq = class_test_oq()
    oq.property_testing()
    return oq.return_bool()

def test_all():
    print(test_stack())
    print(test_queue())
    print(test_oq())
test_all()


