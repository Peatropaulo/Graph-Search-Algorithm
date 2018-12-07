import random
import Queue
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''
queueBFS = Queue.Queue(0)
queueDFS = Queue.LifoQueue(0)
q1 = Queue.PriorityQueue(0)
q = Queue.PriorityQueue(0)

def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
     queueBFS.put((node_id, parent_node_id))
     return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    return queueBFS.empty();

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    (node_id, parent_node_id) = queueBFS.get()
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    queueDFS.put((node_id, parent_node_id))
    return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
   return queueDFS.empty()

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0)
    (node_id, parent_node_id) = queueDFS.get()
    return (node_id, parent_node_id)

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    q.put((cost, (node_id, parent_node_id)))
    return

'''
UC add to queue 
'''
def is_queue_empty_UC():
     
    # Your code here
    if q.empty():
         return True
    return False

'''
UC pop from queue
'''
def pop_front_UC():
    (cost, (node_id, parent_node_id)) = q.get()
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    q1.put((cost, (node_id, parent_node_id)))
    return

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    if q1.empty():
         return True
    return False

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (cost, (node_id, parent_node_id)) = q1.get()
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    random.seed();
    for x in range(0,n+1):
    	state.append(random.randint(0,n))
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    for x in xrange(0,len(state)):
    	col_curr = state[x]
    	for y in xrange(x+1,len(state)):
    		col_comp = state[y]
    		if(col_curr==col_comp):
    			number_attacking_pairs+=1
    		if(col_curr==col_comp+y-x):
    			number_attacking_pairs+=1
    		if(col_curr==col_comp+x-y):
    			number_attacking_pairs+=1
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = state
    new_state = state
    num_atk = 0
    num_atk = comp_att_pairs(state)
    for x in xrange(len(state)-1,0,-1):
        for y in xrange(0,len(state)-2,1):
            state[x] = (state[x]+1)%len(state)
            temp_atk = comp_att_pairs(state)
            if(temp_atk < num_atk):
                num_atk = temp_atk 
                final_state = state
    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    old_state =[]
    count = 0
    count1 = 0
    new_state = get_rand_st(n);
    while (comp_att_pairs(new_state)!=0):
        old_state = new_state
   	new_state = hill_descending(old_state,comp_att_pairs)
   	count += 1
        if( new_state == old_state and (count%3==0)):
            count1 += 1
   	    new_state = get_rand_st(n)
    print(count1)
    return new_state
