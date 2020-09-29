import random  as r
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def walk(n,p):
    start=r.randint(0,n-1)
    g=nx.erdos_renyi_graph(n,p)
    count =0
    s=set()
    v=start
    while len(s)<n:
        count=count+1
        nbr=nx.neighbors(g,v)
        graph=[]
        for x in nbr:
            graph.append(x)
        ran=r.choice(graph)
        v=ran
        s.add(ran)
        
    return count

avg=[]
for x in range(20,300):
    z=[]
    for j in range(10):
         z.append(walk(x,0.3))
    avg.append(np.average(z))
    print x,'->',avg[-1]

plt.plot(range(20,300),avg)
plt.show()
        
        
