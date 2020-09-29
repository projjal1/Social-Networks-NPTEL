import networkx as nx
import matplotlib.pyplot as plt
import random as r


def homo(g,n):
    ls=list(g.nodes())
    
    for i in range(len(ls)):
        g.add_edge(ls[i],ls[i-1])
        g.add_edge(ls[i],ls[i-2])
        c,d=i+1,i+2
        if c==n:
            c=0
        if d==n:
            d=0
        if d==n+1:
            d=1
        g.add_edge(ls[i],ls[c])
        g.add_edge(ls[i],ls[d])
            
def long_tie(g):
    v1=0
    v2=0
    ls=list(g.nodes())
    while(v1==v2):
        v1=r.choice(ls)
        v2=r.choice(ls)
        
    g.add_edge(v1,v2)

def main():
    g=nx.Graph()
    n=input('Enter the no. of nodes:')
    for each in range(n):
        g.add_node(each)
    
    
    homo(g,n)
    
    x=[]
    t=0
    y=[]
    while(t<=100):
        long_tie(g)
        x.append(t)
        t+=1
        y.append(nx.diameter(g))
        
    plt.plot(x,y)
    plt.xlabel('No. of weak ties')
    plt.ylabel('Diameter of the network')
    plt.title('The change in diameter of the network')
    plt.show()
    
    
main()