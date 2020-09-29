import networkx as nx
import matplotlib.pyplot as plt
import itertools as it

def brute(g):
    nodes=g.nodes()
    n=len(g)
    
    first=list()
    second=list()
    
    for i in range(1,n/2+1):
        first.extend(it.combinations(nodes,i))
        
        
    for j in range(len(first)):
        second.append(tuple(set(nodes)-set(first[j])))
        
    intra=list()
    inter1=list()
    inter2=list()
    
    for i in range(len(first)):
        data=nx.subgraph(g,first[i])
        inter1.append(data.number_of_edges())

    
    for i in range(len(second)):
        data=nx.subgraph(g,second[i])
        inter2.append(data.number_of_edges())
        
    
    for i in range(len(first)):
        intra.append(g.number_of_edges()-inter1[i]-inter2[i])
        
    
    ratio=list()
    
    for i in range(len(first)):
        ratio.append((inter1[i]+inter2[i])/intra[i])
    
    index=max(ratio)
    index=ratio.index(index)
    
    print "The first community is :", first[index]
    
    print "The second community is :",second[index]
   
    
g=nx.gnp_random_graph(10,0.35)
nx.draw(g,with_labels=1)
plt.show()

brute(g)


