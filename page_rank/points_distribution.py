import networkx as nx
import matplotlib.pyplot as plt 
import random as r 
import numpy as np

def add_edge(g,p):
    #p is the probabilisatic model
    for u in g.nodes():
        for v in g.nodes():
            if u!=v:
                ran=r.randint(0,1)
                if ran<=p:
                    g.add_edge(u,v)
                else:
                    continue
    return g

def points(n): #Assign the initial points to each nodes here 100
    assign=[100 for ele in range(n)]
    return assign
    
def distribute(g,point):
    new_point=[0 for ele in range(len(g))]
    prev_point=point
    
    for var in g.nodes():
        print g.nodes()
        out=g.out_edges(var)
        if len(out)==0:
            new_point[var]+=prev_point[var]
        else:
            share=float(prev_point[var])/len(out)
            for ele in out:
                print ele[1]
                new_point[ele[1]]+=share
    return new_point

def distribute_points(g,point,limit):
    prev_point=point
    for ele in range(limit):
        new_point=distribute(g,prev_point)
        prev_point=new_point
    return new_point

def sort(point):
    pnt=np.array(point)
    sorted=np.argsort(-pnt)
    return sorted
    
def check(s,p):
    for each in range(len(s)):
        if s[each]!=p[each][0]:
            return False
    return True

n=15
g=nx.DiGraph()
for ele in range(n):
    g.add_node(ele)

g=add_edge(g,0.3)
point=points(n)
d_point=distribute_points(g,point,50)

sorted_nodes=sort(d_point)

pr=nx.pagerank(g)
pr_sorted=sorted(pr.items(),key=lambda x:x[1],reverse=True)


print 'Sorted nodes: using my method'
print sorted_nodes
print 'Sorted nodes: using inbuilt pagerank'
for i in pr_sorted:
    print i[0],
    
print '\nsimilarity: ',check(sorted_nodes,pr_sorted)

