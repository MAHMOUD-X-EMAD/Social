#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import random
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[5]:


def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'asleep'
    return state


# In[6]:


initial_state(G)


# In[7]:


P_AWAKEN = 0.2
def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'asleep':
            if random.random() < P_AWAKEN:
                next_state[node] = 'awake'
    return next_state


# In[8]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[11]:


from simulation import Simulation

sim = Simulation(G, initial_state, state_transition, name='Simple Sim')


# In[12]:


sim.state()


# In[13]:



sim.draw()


# In[14]:


sim.run()


# In[15]:



sim.steps


# In[16]:


sim.draw(with_labels=True)


# In[17]:


sim.state()


# In[18]:


sim.run(10)
sim.steps


# In[19]:


sim.draw(with_labels=True)


# In[20]:


sim.plot()


# In[21]:



sim.draw(4, with_labels=True)


# In[22]:


sim.state(4)


# In[23]:


sim.plot(min_step=2, max_step=8)


# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[25]:


import random
import string

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = random.choice('ABCD')
    return state


# In[26]:



initial_state(G)


# In[27]:


def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        # Caveat: what if the node has no neighbors?
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


# In[28]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[29]:


import matplotlib.pyplot as plt

sim = Simulation(G, initial_state, state_transition, name='Voter Model')


# In[30]:


sim.draw()


# In[31]:


sim.run(40)
sim.draw()


# In[32]:



sim.plot()


# In[33]:


import random

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


# In[34]:


def state_transition_async(G, current_state):
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[35]:


def state_transition_async(G, current_state):
    # Randomizing the update order prevents bias
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[36]:


sim = Simulation(G, initial_state, state_transition_async, name='Async Voter Model')
sim.run(40)
sim.plot()


# In[37]:


def stop_condition(G, current_state):
    unique_state_values = set(current_state.values())
    is_stopped = len(unique_state_values) <= 1
    return is_stopped


# In[38]:


sim = Simulation(G, initial_state, state_transition, stop_condition, name='Voter model')
sim.run(100)


# In[39]:


sim.steps


# In[40]:



sim.plot()


# In[41]:


def state_transition_async_rewiring(G, current_state):
    # Randomizing the update order prevents bias
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            # This is the same as before
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
            # This is the new part
            neighbor = random.choice(list(G.neighbors(node)))
            if current_state[node] != current_state[neighbor]:
                G.remove_edge(node, neighbor)
            
    return current_state


# In[42]:


sim = Simulation(G, initial_state, state_transition_async_rewiring, stop_condition,
                 name='Voter Model with rewiring')
sim.draw()


# In[43]:


sim.run(40)
sim.draw()


# In[44]:



sim.plot()


# In[45]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[46]:


import random

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'S'
    
    patient_zero = random.choice(list(G.nodes))
    state[patient_zero] = 'I'
    return state


# In[47]:



initial_state(G)


# In[48]:


MU = 0.1
BETA = 0.1

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'I':
            if random.random() < MU:
                next_state[node] = 'S'
        else: # current_state[node] == 'S'
            for neighbor in G.neighbors(node):
                if current_state[neighbor] == 'I':
                    if random.random() < BETA:
                        next_state[node] = 'I'

    return next_state


# In[49]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[50]:


sim = Simulation(G, initial_state, state_transition, name='SIS model')
sim.draw()


# In[51]:


sim.run(25)
sim.draw()


# In[52]:


sim.plot()


# In[ ]:




