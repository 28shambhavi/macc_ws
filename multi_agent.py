import numpy as np
import pdb
import networkx as nx

def find_total_steps(di_tree, steps, structure):
    agents = np.zeros(len(steps))
    max_agents = 6
    timestep = 0
    height_map = np.zeros((len(structure), len(structure[0])))
    current_tree = 0
    i = 0
    for step in steps:
        for s in step:
            for pos in s:
                timestep+=1        
    print("\n timesteps", 2*timestep)
    return agents

def make_parallel(di_tree, actions, structure):
    action_list = []
    for a in actions:
        if len(action_list)>0:
            for act in action_list:
                for ancestor in nx.ancestors(di_tree, (act[0], act[1])):   
                    if (a[1][0], a[1][1])==ancestor:
                        pass
                    else:
                        pass
                        #print("can be made parallel if same tree", (a[1][0], a[1][1]), (act[0], act[1]))
                        # same step tree
                        
                        # max agents

                        # say parallel possible

        action_list.append(a[1])    
            
    # p_episodes = []
    # flag = 0
    # max_agents = 6
    # num_episodes = 10
    # tree = 'pos'
    # for i in range(0, num_episodes):
    #     p_episodes.append([])
    # for event in event_tree:
    #     if tree==event[0]:
    #         for i in range(0, num_episodes):
    #             flag = 0
    #             if len(p_episodes[i])<max_agents:
    #                 for pos in event[2]:
    #                     #checking if pos is being used by another agent
    #                     if pos in p_episodes[i]:
    #                         flag = 1
    #                     elif pos[2]>0:
    #                         for k in range(0, pos[2]):
    #                             if (pos[0], pos[1], pos[2]-k) in p_episodes[k]:
    #                                 flag = 1
    #                 if flag==0:
    #                     p_episodes[i].append((event[0], event[1]))
    #                     tree = event[0]
    #                     flag = 0
    #                     break 
    #                 else: 
    #                     continue
    #     else:
    #         for i in range(0, num_episodes):
    #             if len(p_episodes[i])<max_agents:
    #                 print(len(p_episodes[i]), "len of episode", max_agents, "max agents")
    #                 p_episodes[i].append((event[0], event[1]))
    #     tree = event[0]
    #     flag = 0
    # return p_episodes