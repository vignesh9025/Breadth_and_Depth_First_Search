# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- IMPLEMENTATION OF BREADTH-FIRST AND DEPTH-FIRST SEARCH ------------------------------------------------------
# ------------------------------- AUTHOR: VIGNESH M. PAGADALA ---------------------------------------------------------------------------------
# --------------------------------FILE: Week1_BFS_and_DFS.py ----------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------- DEFINE PUZZLES, TREES AND GRAPHS TO SEARCH HERE -------------------------------------------------------------

# EXAMPLE 1
import copy
successors = {'a':  ['b', 'c', 'd'],
              'b':  ['e', 'f', 'g'],
              'c':  ['a', 'h', 'i'],
              'd':  ['j', 'z'],
              'e':  ['k', 'l'],
              'g':  ['m'],
              'k':  ['z']}

def successorsf(state):
    return copy.copy(successors.get(state, []))

# EXAMPLE 2

def gridSuccessors(state):
    row, col = state
    # succs will be list of tuples () rather than list of lists [] because state must
    # be an immutable type to serve as a key in dictionary of expanded nodes
    succs = []
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            newr = row + r
            newc = col + c
            if 0 <= newr <= 9 and 0 <= newc <= 9:  # cool, huh?
                succs.append( (newr, newc) )
    return succs

# EXAMPLE 3

successors2 = {'a':  ['b', 'c', 'd', 'e'],
              'b':  ['e', 'f'],
              'c':  ['g', 'h'],
              'd':  ['h', 'i'],
              'e':  ['i', 'j'],
              'f':  ['k'],
              'g':  ['k', 'l'],
              'h':  ['l'],
              'i':  ['m'],
              'j':  ['m', 'n'],
              'l':  ['z'],
              'm':  ['z']}

def successorsf2(state):
    return copy.copy(successors2.get(state, []))

# EXAMPLE 4

successors3 = { 1:  [2, 3, 4],
               2:  [5],
               3:  [6, 7]}

def successorsf3(state):
    return copy.copy(successors3.get(state, []))

# EXAMPLE 5

successors4 = {}
def successorsf4(state):
    return copy.copy(successors4.get(state, []))

# EXAMPLE 6

successors5 = { 1.5:  [2.5, 3.5, 4.5],
               2.5:  [5.5],
               3.5:  [6.5, 7.5]}

def successorsf5(state):
    return copy.copy(successors5.get(state, []))

# EXAMPLE 6

successors7 = {}
def successorsf7(state):
    return copy.copy(successors7.get(state, []))

# EXAMPLE 7

successors8 = {'a':  ['c', 'b', 'd'],
              'b':  ['f', 'e', 'g'],
              'c':  ['i', 'h', 'a'],
              'd':  ['z', 'j'],
              'e':  ['k', 'l'],
              'g':  ['m'],
              'k':  ['z']}

def successorsf8(state):
    return copy.copy(successors8.get(state, []))



# ------------------------------- BREADTH-FIRST SEARCH ----------------------------------------------------------------------------------------

def breadthFirstSearch(startState, goalState, successorsf):
    
    # We firstly initialize expanded to an empty dictionary and 
    # unExpanded to be a list containing the tuple (startState, 'None'), which refers to the root node.
    
    expanded = {}
    unExpanded = [(startState, 'None')]
    
    # Next, we check if the goal specified is the same as the root node, in which case, the root node (*startState*) 
    # is returned as a list. 
    
    if(startState == goalState):
        return list(startState)
    
    if not successorsf(startState):
        return 'No nodes present'
    # Then we begin iterating through *unExpanded* while it's not empty. This is done with a while loop.
    
    while(unExpanded):
        
        # We pop from the end of *unExpanded* and initialize the (child, parent) tuple to *statePair*. 
        # The variable *statePair* is used in order to be able to insert the (child, parent) tuple into the dictionary 
        # *expanded* as child:parent pairs. The parent of each node is included so that we can trace back the path to the root
        # once the goal is found. 
        
        statePair = unExpanded.pop()
        expanded[statePair[0]] = statePair[1]
        state = statePair[0]
        
        # Children of *state* are obtained using the *successorsf* function, and are stored in the variable *children*.  
        
        children = successorsf(state)

        
        # After this, children which are already present in either *expanded* or *unExpanded* are removed for efficiency.
        
        unexp = []
        for tup in unExpanded:
            unexp.append(tup[0])
        exp = list(expanded.keys())
        for x in exp:
            if x in children:
                children.remove(x)
        for x in unexp:
            if x in children:
                children.remove(x)
        
        # Sorting children to get the right order
        children = sorted(children)

        # We now iterate through the *children* list to search for a goal.
        
        for child in children:
            
            # If the goal state is found, then we loop through *expanded* to find the path to the root. 
            # This is done with a while loop, and at each iteration, we find the parent of *state* and append 
            # it to the list *solPath*, and *state* is updated to the parent. The loop stops when *state* = 'None' 
            # which would imply that the root node has been reached.
            
            if(child == goalState):
                solPath = [goalState, state]
                while(expanded[state] != 'None'):
                    parentNew = expanded[state]
                    solPath.append(parentNew)
                    state = parentNew
                    
                # *solPath* is reversed so that it's displayed in the right order and returned.
                
                solPath.reverse()
                return solPath
            
            # If no goal state was found in the current iteration, then the children are inserted into *unExpanded* 
            # list at the front, as a (child, state) tuple.
            
            unExpanded.insert(0, (child, state))
            
    # If no goal could be found, then *unExpanded* becomes empty and the outer while loop is exited.
    
    return 'Goal not found.'

# ------------------------------- DEPTH-FIRST SEARCH ------------------------------------------------------------------------------------------

def depthFirstSearch(startState, goalState, successorsf):
    
    # We firstly initialize expanded to an empty dictionary and 
    # unExpanded to be a list containing the tuple (startState, 'None'), which refers to the root node.
    
    expanded = {}
    unExpanded = [(startState, 'None')]
    
    # Next, we check if the goal specified is the same as the root node, in which case, the root node (*startState*) 
    # is returned as a list.
    
    if not successorsf(startState):
        return 'No nodes are present'

    if(startState == goalState):
        return startState

    # Then we begin iterating through *unExpanded* while it's not empty. This is done with a while loop.
    
    while(unExpanded):
        
        # We pop from the end of *unExpanded* and initialize the (child, parent) tuple to *statePair*. 
        # The variable *statePair* is used in order to be able to insert the (child, parent) tuple into the dictionary 
        # *expanded* as child:parent pairs. The parent of each node is included so that we can trace back the path to the root
        # once the goal is found.
        
        statePair = unExpanded.pop()
        expanded[statePair[0]] = statePair[1]
        state = statePair[0]
        
        # Children of *state* are obtained using the *successorsf* function, and are stored in the variable *children*.
        
        children = successorsf(state)
        
        # After this, children which are already present in either *expanded* or *unExpanded* are removed, for efficiency.
        
        unexp = []
        for tup in unExpanded:
            unexp.append(tup[0])
        exp = list(expanded.keys())
        for x in exp:
            if x in children:
                children.remove(x)
        for x in unexp:
            if x in children:
                children.remove(x)
                   
        # Reversal of children list is done to get the right order.
        
        #children = sorted(children)
        children.reverse()
        
        # We now iterate through the *children* list to search for a goal.
        
        for child in children:
            
            # If the goal state is found, then we loop through *expanded* to find the path to the root. 
            # This is done with a while loop, and at each iteration, we find the parent of *state* and append 
            # it to the list *solPath*, and *state* is updated to the parent. The loop stops when *state* = 'None' 
            # which would imply that the root node has been reached.
            
            if(child == goalState):
                solPath = [goalState, state]
                while(expanded[state] != 'None'):
                    parentNew = expanded[state]
                    solPath.append(parentNew)
                    state = parentNew
                    
                # *solPath* is reversed so that it's displayed in the right order and returned.
                
                solPath.reverse()
                return solPath
            
            # If no goal state was found in the current iteration, then the children are inserted into *unExpanded* 
            # list at the rear, as a (child, state) tuple.
            
            unExpanded.append((child, state))
            
    # If no goal could be found, then *unExpanded* becomes empty and the outer while loop is exited.
    
    return 'Goal not found.'

<<<<<<< HEAD
=======
# ------------------------------- WRITE TESTING CODE HERE --------------------------------------------------------------

if __name__ == '__main__':
    #print(depthFirstSearch((0,0), (9,9), gridSuccessors))
    
    #print(breadthFirstSearch((0,0), (9,9), gridSuccessors))
    
    #print(breadthFirstSearch('a', 'z', successorsf2))
    #print(depthFirstSearch('a', 'z', successorsf2))
    
    #print(depthFirstSearch(1, 6, successorsf3))    
    
    #print(depthFirstSearch(1, 1, successorsf2))   
    
    #print("BFS")
    #print(breadthFirstSearch('a', 'z', successorsf8))
    print("DFS")
    print(depthFirstSearch('a', 'z', successorsf))




>>>>>>> 50a67395308fcf657b66f9208ed702123cf181b0



