#!/usr/bin/env python
# coding: utf-8

# In[28]:


import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
G = nx.Graph()
nodes_to_add = ['1', '2', '3', '4', '5', '6']
G.add_nodes_from(nodes_to_add)
edges_to_add = [('1', '2'), ('1', '3'), ('4', '1'), ('1', '6'), ('2', '3'), ('2', '4'), ('3', '6')]
G.add_edges_from(edges_to_add)
nx.draw(G, with_labels=True)


# In[40]:


def plot_degree_dist(G):
    
    degrees = G.degree()
    degrees = dict(degrees)
    values = sorted(set(degrees.values()))
    print(values)
    histo = [list(degrees.values()).count(x) for x in values]
    P_k = [x / G.order() for x in histo]
    print(len(P_k))
    
    plt.figure()
    plt.bar(values, P_k)
    plt.xlabel("k",fontsize=20)
    plt.ylabel("p(k)", fontsize=20)
    plt.title("Degree Distribution", fontsize=20)
    
    plt.show()
    plt.figure()
    plt.grid(False)
    plt.loglog(values, P_k, "bo")
    plt.xlabel("k", fontsize=20)
    plt.ylabel("log p(k)", fontsize=20)
    plt.title("log Degree Distribution")
    plt.show()
    plt.show()  


# In[48]:


from collections import Counter
degree_sequence = [G.degree(n) for n in G.nodes]
degree_counts = Counter(degree_sequence)
min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Number of Nodes", fontsize=20)
plot_x = list(range(min_degree, max_degree + 1))
plot_y = [degree_counts.get(x, 0) for x in plot_x]
plt.bar(plot_x, plot_y)


# In[56]:


Adj = nx.adjacency_matrix(G).todense()
plot_degree_dist(G)


# In[57]:


Adj


# In[58]:


D = nx.DiGraph()
nodes_to_add = ['1', '2', '3', '4', '5', '6']
D.add_nodes_from(nodes_to_add)
edges_to_add = [('1', '2'), ('4', '1'), ('2', '3'), ('2', '4'), ('3', '2'), ('3', '1'), ('6', '1'), ('6', '3')]
D.add_edges_from(edges_to_add)
nx.draw(D, with_labels=True)


# In[59]:


from collections import Counter
degree_sequence = [D.degree(n) for n in D.nodes]
degree_counts = Counter(degree_sequence)
min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Number of Nodes", fontsize=20)
plot_x = list(range(min_degree, max_degree + 1))
plot_y = [degree_counts.get(x, 0) for x in plot_x]
plt.bar(plot_x, plot_y)


# In[60]:


Adj = nx.adjacency_matrix(D).todense()
Adj


# In[61]:


plot_degree_dist(D)


# In[ ]:





# In[ ]:




