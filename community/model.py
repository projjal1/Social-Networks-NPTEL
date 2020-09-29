import networkx as nx
import matplotlib.pyplot as plt 

def remove(g):
    dict1=nx.edge_betweenness_centrality(g)
    list_of_tuples=dict1.items()
    list_of_tuples.sort(key=lambda x:x[1],reverse=True)
    return list_of_tuples[0][0]
    

def girvan(g):
    
    c=list(nx.connected_component_subgraphs(g))
    l=len(c)
    print l
    while(l==1):
        g.remove_edge(*remove(g))
        c=list(nx.connected_component_subgraphs(g))
        l=len(c)
        print l
    return c
    
g=nx.gnp_random_graph(10,0.5)
nx.write_gml(g,'case.gml')
nx.draw_shell(g,with_labels=1)
plt.show()
c=girvan(g)
for i in c:
    print i.nodes()

