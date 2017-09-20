# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- IMPLEMENTATION OF BREADTH-FIRST AND DEPTH-FIRST SEARCH USING RECURSION --------------------------------------
# ------------------------------- AUTHOR: VIGNESH M. PAGADALA ---------------------------------------------------------------------------------
# ------------------------------- FILE: Week1_BFS_and_DFS_using_Recursion.py ------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------- DEFINE TREES HERE -------------------------------------------------------------------------------------------

import copy
successors = {'a':  ['b', 'c', 'd'],
              'b':  ['e', 'f', 'g'],
              'c':  ['a', 'h', 'i'],
              'd':  ['j', 'z'],
              'e':  ['k', 'l'],
              'g':  ['m'],
              'k':  ['z']}
successors2 = {'a': ['b', 'c', 'd'],
               'b': ['e', 'f', 'g']}

def successorsf(state):
    return copy.copy(successors.get(state, []))

# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- DEPTH-FIRST SEARCH USING RECURSION --------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

# THINKING RECURSIVELY, WE CAN IMPLEMENT THIS PROBLEM AS, current_node + depthFirstSearch(child_node)

def DFS(state, goal, successorsf, goalPath = [], visited = []):
    visited.append(state)
    # IF I AM THE GOAL, I SHALL APPEND IT TO THE PATH AND RETURN IT
    if state == goal:
        goalPath.append(state)
        return goalPath
    children = successorsf(state)
    for x in visited:
        if x in children:
            children.remove(x)
    for child in children:
        # DO ANY OF THESE HAVE A GOAL?
        goalPath = list(DFS(child, goal, successorsf, goalPath, visited))
        # IF YES, THEN GIVE ME THE PATH. I SHALL APPEND IT TO MYSELF AND RETURN IT
        if goalPath:
            goalPath.append(state)
            return goalPath
    # NONE OF MY CHILDREN HAVE A GOAL, AND I'M NOT A GOAL EITHER. BUT THERE ARE OTHER PARENTS WHOSE CHILDREN MIGHT HAVE GOALS, OR MY SIBLINGS MIGHT BE GOALS.
    return []


# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- BREADTH-FIRST SEARCH USING RECURSION ------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

# IMPLEMENTATION OF BREADTH FIRST SEARCH USING RECURSION.
# THINKING RECURSIVELY, THE ENTIRE PROBLEM CAN BE BROKEN DOWN INTO SUB-PROBLEMS, WHERE GIVEN A NODE, THE OBJECTIVE IS TO FIND OUT ALL IT'S CHILDREN, AND ALSO, THE
# CHILDREN OF IT'S SIBLINGS AS WELL, AND PUT IT INTO A LIST.

def BFS(state, successorsf, siblings = [], path = [], flag = 0):
    # IF NODE IS ROOT NODE, WE ADD IT INTO PATH
    if not path:
        path.append(state)
    # WE SHALL NOW DO 2 THINGS: 1) COMPUTE MY CHILDREN AND ADD IT TO THE PATH. 2) COMPUTE CHILDREN OF MY SIBLINGS AND ADD THEM TO PATH
    childnext = ''
    children = successorsf(state)
    # IF CHILDREN ALREADY IN PATH, REMOVE
    for x in path:
        if x in children:
            children.remove(x)
    # ADD MY OWN CHILDREN TO THE FRONT OF PATH LIST
    for child in children:
        path.append(child)
    # FIND OUT IF THE STATE HAS ANY SIBLINGS, IF SO, THEN OBTAIN SIBLINGS AND ADD TO PATH
    if siblings:
        # REMOVE ITSELF FROM SIBLINGS LIST
        if state in siblings:
            siblings.remove(state)
        # FIND OUT CHILDREN OF SIBLINGS AND APPEND MY SIBLING'S CHILDREN TO PATH
        for sibling in siblings:
            sibChildren = successorsf(sibling)
            # REMOVE ANY NODES ALREADY PRESENT IN PATH
            for x in path:
                if x in sibChildren:
                    sibChildren.remove(x)
            for sibChild in sibChildren:
                path.append(sibChild)
    # NOW ADD CHILDREN TO 'SIBLINGS' SO THAT THE SUCCESSOR NODE CAN FIGURE OUT IT'S SIBLINGS' CHILDREN
    siblings.clear()
    for child in children:
        siblings.append(child)
    # TAKE THE LEFTMOST CHILD
    for child in children:
        childnext = child
        break
    # RECURSIVELY CALL BFS FOR LEFTMOST CHILD IN NEXT LEVEL
    if not children:
        return path
    else:
        path = BFS(childnext, successorsf, siblings, path, flag)
    return path


# ------------------------------- TEST CODE HERE ------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print(BFS('a', successorsf))





