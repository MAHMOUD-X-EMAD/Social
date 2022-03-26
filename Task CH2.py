#!/usr/bin/env python
# coding: utf-8

# In[9]:


import networkx as nx
G = nx.Graph()

G.add_nodes_from([1,2,3,4])

G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])

nx.draw(G, with_labels=True)


# In[10]:


nx.has_path(G, 3, 4)


# In[11]:


list(nx.all_simple_paths(G, 3, 4))


# In[12]:


nx.shortest_path(G, 3, 4)


# In[13]:


nx.shortest_path_length(G, 3, 4)


# In[14]:


nx.is_connected(G)


# In[17]:


G = nx.Graph()

nx.add_cycle(G,(1,2,3))
G.add_edge(4,5)

nx.draw(G, with_labels=True)


# In[18]:


nx.is_connected(G)


# In[19]:


nx.has_path(G, 3, 5)


# In[20]:


nx.shortest_path(G, 3, 5)


# In[21]:


nx.number_connected_components(G)


# In[22]:


list(nx.connected_components(G))


# In[23]:


components = list(nx.connected_components(G))
len(components[0])


# In[24]:


max(nx.connected_components(G), key=len)


# In[25]:


core_nodes = max(nx.connected_components(G), key=len)
core = G.subgraph(core_nodes)

nx.draw(core, with_labels=True)


# In[26]:


D = nx.DiGraph()
D.add_edges_from([
    (1,2),
    (2,3),
    (3,2), (3,4), (3,5),
    (4,2), (4,5), (4,6),
    (5,6),
    (6,4),
])
nx.draw(D, with_labels=True)


# In[27]:


nx.has_path(D, 1, 4)


# In[28]:


nx.has_path(D, 4, 1)


# In[29]:


nx.shortest_path(D, 2, 5)


# In[30]:


nx.shortest_path(D, 5, 2)


# In[31]:


nx.is_strongly_connected(D)


# In[32]:


nx.is_weakly_connected(D)


# In[33]:


nx.is_connected(D)


# In[34]:


list(nx.weakly_connected_components(D))


# In[35]:


list(nx.strongly_connected_components(D))


# In[39]:


G = nx.read_graphml('C:\Users\20106\Downloads\openflights_usa.graphml')


# In[40]:


G.nodes['IND']


# In[ ]:




