import networkx as nx
import matplotlib.pyplot as plt
import random as r

def disp(g,ne,ind):
    if ne=='':
        ne=[]
    pos=nx.circular_layout(g)
    node=g.nodes()
    old_edge=list(set(g.edges())-set(ne))
    nx.draw_networkx_nodes(g,pos,nodelist=node,node_color="r")
    nx.draw_networkx_edges(g,pos,edgelist=old_edge,edge_color="blue")
    nx.draw_networkx_edges(g,pos,edgelist=ne,edge_color="g",style="dashdot")
    plt.savefig(str(ind))
    plt.close()
    
def erdos(g,p):
    con_edge=0
    for i in g.nodes():
        for u in g.nodes():
            if i!=u:
                val=r.random()
                if (val<=p):
                    flag=g.has_edge(i,u)
                    if flag==True:
                        continue
                    else:
                        g.add_edge(i,u)
                        con_edge+=1
                        disp(g,[(i,u)],con_edge)
                        
    
    print 'Connected edges are: ',con_edge
            
    
    
def main():
    '''n=input('Enter the value of nodes:')
    p=input('Enter the value of probability:')'''
    n=40
    p=0.2
    g=nx.Graph()
    for i in range(n):
        g.add_node(i)
    
    disp(g,'',-1)
    erdos(g,p)
    
main()

