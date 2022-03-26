#!/usr/bin/env python
# coding: utf-8

# In[42]:


import networkx as nx
G = nx.Graph()
def get_leaves(G):
    j=0
    final=[]
    leaves=[G.degree(n) for n in G.nodes()]
    nodes=G.nodes
    print(nodes)
    print(leaves)
    for i in range(nodes):
        if leaves[i]==1:
            final[i]=nodes[i]
        
    return final 

G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
f=get_leaves(G)
print(f)
nx.draw(G)


# In[50]:


def max_degree(G):
    max=G.degree('a')
    for i in G.nodes:
        if max<G.degree(i):
            max=G.degree(i)
    return max

G=nx.Graph()
G.add_edges_from([('a','b'),('b','c'),('c','d'),('a','d')])
max_degree(G)


# In[52]:


def mutual_friends(G, node_1, node_2):
    list1=list(G.neighbors(node_1))
    list2=list(G.neighbors(node_2))
    final=[]
    for i in range(list1):
        for j in range(list2):
            if list1[i]==list2[j]:
                final[i]=list1[i]
        
            
    return final    
    
G=nx.Graph()
G.add_edges_from([('a','b'),('b','c'),('c','d'),('a','d')])
mutual_friends(G,'a','b')


# In[ ]:




