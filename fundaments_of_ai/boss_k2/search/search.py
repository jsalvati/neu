# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class Node:
    
    def __init__(self, state, parent, children):
        self.state  = state
        self.parent = parent
        self.children = children
        self.action = None
        self.cost = 0



class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """

    frontier = util.Stack()
    frindgeStates = []
    explored = []
    actions = []
    node = Node(problem.getStartState(), None, [])
    frontier.push(node)
    frindgeStates.append(node.state)
    
    while 1:
        if frontier.isEmpty():
            return actions
            
        node = frontier.pop()

        if(problem.isGoalState(node.state)):
            actions = solution(problem, node)
            print "Found goal!!! :",explored
            return actions

        explored.append(node.state)

        for childNode in problem.getSuccessors(node.state):
            
            state,action,cost = childNode

            if ( (not state in explored) ):
                child = Node(state,node,[])
                child.action = action
                child.cost = cost

                node.children.append(child)
                frontier.push(child)
                frindgeStates.append(child.state)


def isChildInFrontier (child, frontier):
    for node in frontier:
        if child.state == node.state:
            return True
    return False

def isChildInFrontierHeap (child, frontier):
    for something,cost,node in frontier:
        if child.state == node.state:
            return True
    return False

def findChildInFrontier (child, frontier):
    for something,cost,node in frontier:
        if child.state == node.state:
            return node
    return -1


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""


    frontier = util.Queue()
    explored = []
    actions = []
    node = Node(problem.getStartState(), None, [])
    frontier.push(node)
    
    while 1:
        if frontier.isEmpty():
            print "Frontier is empty :-("
            return actions
            
        node = frontier.pop()
        #print "Node state when popin: ",node.state

        if(problem.isGoalState(node.state)):
            actions = solution(problem, node)
            #print "Found goal!!! :",explored
            return actions

        explored.append(node.state)
        for childNode in problem.getSuccessors(node.state):
            
            state,action,cost = childNode
            child = Node(state,node,[])
            child.action = action
            child.cost = cost

            if ( (not state in explored) and (not isChildInFrontier(child, frontier.list))):
                #print state
                node.children.append(child)
                frontier.push(child)
                    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    frontier = util.PriorityQueue()

    explored = []
    actions = []
    node = Node(problem.getStartState(), None, [])
    frontier.push(node,0)
    
    while 1:
        if frontier.isEmpty():
            return actions
            
        node = frontier.pop()

        if(problem.isGoalState(node.state)):
            actions = solution(problem, node)
            return actions

        explored.append(node.state)
        for childNode in problem.getSuccessors(node.state):
            
            state,action,cost = childNode
            
            child = Node(state,node,[])
            child.action = action
            child.cost = node.cost + cost

            existingChild = findChildInFrontier(child, frontier.heap)

            if ( (not state in explored) and (existingChild == -1)):
                node.children.append(child)
                frontier.push(child,child.cost)
            
            elif ((existingChild != -1) and ( existingChild.cost > child.cost)):
                #cheaper path, update frontier
                existingChild.parent = node
                existingChild.cost = cost
                existingChild.action = action




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
            
    frontier = util.PriorityQueue()

    explored = []
    actions = []
    node = Node(problem.getStartState(), None, [])
    frontier.push(node, 0)
    
    while 1:
        if frontier.isEmpty():
            return actions
            
        node = frontier.pop()

        if(problem.isGoalState(node.state)):
            actions = solution(problem, node)
            return actions

        explored.append(node.state)
        for childNode in problem.getSuccessors(node.state):

            state,action,cost = childNode
            
            child = Node(state,node,[])
            child.action = action
            child.cost = node.cost + cost
            child.estimation = child.cost + heuristic(child.state, problem)

            existingChild = findChildInFrontier(child, frontier.heap)

            if ( (not state in explored) and (existingChild == -1)):
                node.children.append(child)
                frontier.push(child,child.estimation)
                #frontier.print_heap()
            
            elif ((existingChild != -1) and ( existingChild.cost > child.cost)):
                #cheaper path, update frontier
                existingChild.parent = node
                existingChild.cost = cost
                existingChild.action = action
                
                #?? this should update the list, not add a new one...
                frontier.push(existingChild,child.estimation) 


def solution(problem, node):
    """ 
    starting with a solution node, keep adding the action to the end of the actions list
    until we reach the start state of the problem
    """
 
    actions = []
    while (node.state != problem.getStartState()):
        actions = [node.action] + actions 
        node = node.parent

    return actions

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
