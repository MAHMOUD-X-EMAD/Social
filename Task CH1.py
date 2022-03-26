#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx


# In[2]:


G = nx.Graph()

G.add_node('a')

nodes_to_add = ['b', 'c', 'd']
G.add_nodes_from(nodes_to_add)

G.add_edge('a', 'b')

edges_to_add = [('a', 'c'), ('b', 'c'), ('c', 'd')]
G.add_edges_from(edges_to_add)

nx.draw(G, with_labels=True)


# In[3]:


nx.draw(G,
        with_labels=True,
        node_color='blue',
        node_size=1600,
        font_color='white',
        font_size=16,
        )


# In[5]:


G.nodes()
G.edges()
for node in G.nodes:
    print(node)
for edge in G.edges:
    print(edge)

G.number_of_nodes()


# In[6]:


G.number_of_edges()


# In[7]:


G.neighbors('b')


# In[8]:


list(G.neighbors('b'))


# In[9]:


nx.is_tree(G)
nx.is_connected(G)


# In[10]:


nx.is_tree(G)


# In[11]:


G.has_node('a')


# In[12]:


'd' in G.nodes


# In[13]:


G.has_edge('a', 'b')


# In[14]:


('c', 'd') in G.edges


# In[15]:


len(list(G.neighbors('a')))


# In[16]:


G.degree('a')


# In[17]:


items = ['spider', 'y', 'banana']
[item.upper() for item in items]


# In[18]:


print(G.nodes())
print([G.degree(n) for n in G.nodes()])


# In[19]:


g = (len(item) for item in items)
list(g)


# In[20]:


max(len(item) for item in items)


# In[21]:


sorted(item.upper() for item in items)


# In[22]:


G = nx.Graph()

G.add_nodes_from(['cat','dog','virus',13])

G.add_edge('cat','dog')

nx.draw(G, with_labels=True, font_color='white', node_size=1000)


# In[23]:


print(open('../datasets/friends.adjlist').read())


# In[24]:


D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])

nx.draw(D, with_labels=True)


# In[25]:


D.has_edge(1,2)


# In[26]:


D.has_edge(2,1)


# In[27]:


print('Successors of 2:', list(D.successors(2)))

print('Predecessors of 2:', list(D.predecessors(2)))


# In[28]:


D.in_degree(2)


# In[29]:


print('Successors of 2:', list(D.successors(2)))
print('"Neighbors" of 2:', list(D.neighbors(2)))


# In[ ]:




