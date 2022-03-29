#!/usr/bin/env python
# coding: utf-8

# In[6]:


import networkx as nx

G = nx.read_graphml('openflights_usa.graphml')

nx.draw(G, with_labels=True)


# In[7]:


print(G.nodes['FAI']) 
print(G.nodes['IND'])
nx.has_path(G, 'IND', 'FAI')  


# In[8]:


nx.shortest_path(G ,'IND', 'FAI')


# In[9]:


nx.is_connected(G)


# In[ ]:




