import networkx as nx
import matplotlib.pyplot as plt
import random as r


def display(g,i,ne,string):
    if (i==''  and ne==''):
        prev_node=g.nodes()
        new_node=[]
        prev_edge=g.edges()
        new_edge=[]
    else:
        new_node=[i]
        new_edge=ne
        prev_edge=list(set(g.edges())-set(new_edge)-set([(b,a) for (a,b) in new_edge]))
        prev_node=list(set(g.nodes())-set(new_node))
    
    pos=nx.circular_layout(g)
    nx.draw_networkx_nodes(g,pos,nodelist=prev_node,node_color='r')
    nx.draw_networkx_nodes(g,pos,nodelist=new_node,node_color='g')
    nx.draw_networkx_edges(g,pos,edgelist=prev_edge,edge_color='r')
    nx.draw_networkx_edges(g,pos,edgelist=new_edge,edge_color='g',style='dashdot')
    plt.savefig(str(string))
    plt.close()
    
def node_barabasi(g,n,m0):
    m=m0-1
    ref=0
    
    for var in range(m0+1,n+1):
        
        ref+=1
        g.add_node(var)
        
        deg=nx.degree(g)
        prob={}
        
        sum=0
        for n,p in deg:
            sum+=p
        
        for each in g.nodes():
            prob[each]=float(deg[each])/float(sum)
        
        cum_prob=[]
        index=0
        for n,f in prob.items():
            temp=[n,index]
            index+=f
            cum_prob.append(temp)
            
        new_edge=[]
        no_edge=0
        target_node=[]
        
        k=0
        while(no_edge<m):
            no=r.random()
            prev_cum=0
            k=0
            while(not(no>prev_cum  and no<=cum_prob[k][1])):
                prev_cum=cum_prob[k][1]
                k+=1
            
            node=cum_prob[k][0]
            
            print node
            
            if node in target_node:
                continue
            else:
                target_node.append(node)
            g.add_edge(var,node)
            no_edge+=1
            new_edge.append((var,node))
            
        display(g,var,new_edge,ref)
        print var-m0,' node added'            
            
        

def main():
    '''n=input('Enter the value of n')'''
    n=20
    m0=r.randint(3,n/5)
    g=nx.path_graph(m0)
    display(g,'', '',0)
    node_barabasi(g,n,m0)

main()


