import networkx as n
import matplotlib.pyplot as plt
import random_walk as p

g=n.DiGraph()
for ele in range(4):
    g.add_node(ele)

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,0)
g.add_edge(2,3)


nx.draw(g,with_labels=1)
plt.show()

points=[20,30,60,20]
new_point=p.walk(g,points)

print new_point
