import networkx as nx
import random as r
import numpy as np


def add_edge(g,p):
    for u in g.nodes():
        for v in g.nodes():
            if u!=v:
                ran=r.randint(0,1)
                if ran<=p:
                    g.add_edge(u,v)
    return g

def walk(g,point):
    nd=g.nodes()
    node=[x for x in nd]
    ran=r.choice(node)
    out=[x[1] for x in g.out_edges(ran)]
    
    point[ran]+=1
    for ele in range(2):
        if len(out)==0:
            focus=r.choice(nd)
        else:
            r_nei=r.choice(out)
            focus=r_nei
        point[focus]+=1
        out=[x[1] for x in g.out_edges(ran)]
    print point
    return point

n=10
g=nx.DiGraph()
for var in range(n):
    g.add_node(var)
g=add_edge(g,0.5)
point=[0 for ele in range(n)]
points=walk(g,point)
temp=np.array(points)
result=np.argsort(-temp)
print result

pr=nx.pagerank(g)


sort=sorted(pr.items(),key = lambda x:x[1] , reverse=True)
array=[x[0] for x in sort]
print array


import networkx as nx
import random as r
import numpy as np


def add_edge(g,p):
    for u in g.nodes():
        for v in g.nodes():
            if u!=v:
                ran=r.randint(0,1)
                if ran<=p:
                    g.add_edge(u,v)
    return g

def walk(g,point):
    nd=g.nodes()
    node=[x for x in nd]
    ran=r.choice(node)
    out=[x[1] for x in g.out_edges(ran)]
    
    point[ran]+=1
    for ele in range(2):
        if len(out)==0:
            focus=r.choice(nd)
        else:
            r_nei=r.choice(out)
            focus=r_nei
        point[focus]+=1
        out=[x[1] for x in g.out_edges(ran)]
    print point
    return point

n=10
g=nx.DiGraph()
for var in range(n):
    g.add_node(var)
g=add_edge(g,0.5)
point=[0 for ele in range(n)]
points=walk(g,point)
temp=np.array(points)
result=np.argsort(-temp)
print result

pr=nx.pagerank(g)


sort=sorted(pr.items(),key = lambda x:x[1] , reverse=True)
array=[x[0] for x in sort]
print array