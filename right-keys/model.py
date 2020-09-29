import networkx as nx
import matplotlib.pyplot as plt

    
def kshell(g,k):
    temp=[]
    flag=1
    while(flag!=0):
        tmp=[]
        deg=list(g.degree())
        count=0
        for node,each in deg:
            if each<=k:
                count+=1
                tmp.append(node)
        
        for each in tmp:
            temp.append(each)
            g.remove_node(each)
            nx.draw(g,with_labels=1)
            plt.show()
        
        
        if count==0:
            flag=0
    
    return temp
    
def mod(g):
    k=1
    while(len(g)!=0):
        print k,' shell:',kshell(g,k)
        k+=1
    

ref=0    
g=nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
g.add_node(7)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(3,4)
g.add_edge(3,2)
g.add_edge(4,2)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(6,7)

nx.draw(g,with_labels=1)
plt.show()
mod(g)