# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        newFoodList = newFood.asList()

        score = 100

        '''
        print "newPos: ",newPos
        print "newFood: ",newFoodList
        print "newGhostStates: ",newGhostStates
        print "ghostPos : ",newGhostStates
        print "newScaredTimes: ",newScaredTimes
        '''

        i = 0
        for state in newGhostStates:
            #if newScaredTimes[i] > 0:
            #    score += 100
            
            if (newPos == state.getPosition()):
                #print "ghost is super close!!"
                score += -40
            if (pacmanNearGhost(newPos, state.getPosition())):
                #print "ghost is kinda close!!"
                score += -20

            i += 1

        if list(newPos) in newFoodList:
            print "food is adjacent!!"
            score += 20
        else:
            score += movingTorwardsClosestFood(currentGameState.getPacmanPosition(), newPos, newFoodList)

        #print score

        return score

def movingTorwardsClosestFood (currentPos, newPos, newFoodList):

    #find closestFood
    '''
    if(len(newFoodList)):
        distance, food = min([(util.manhattanDistance(newPos, food) , food) for food in newFoodList])
        if distance == 1:
            return 10
        else:
            return (util.manhattanDistance(currentPos,food) - distance)*2
    '''
    if(len(newFoodList)):
        distance, food = min([(util.manhattanDistance(currentPos, food) , food) for food in newFoodList])

        if (util.manhattanDistance(newPos, food)) < distance:
            return 10
        else:
            return -3
    
    
    return 0


def pacmanNearGhost(newPos, ghostPos):

    x1,y1 = newPos
    x2,y2 = ghostPos

    dx = abs(x2-x1)
    dy = abs(y2-y1)
    
    close = (((dx <= 2) and (dy == 0)) or \
             ((dy <= 2) and (dx == 0)) or \
             ((dx == 1) and (dy == 1)) )

    print dx,dy

    return close

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """

        
        action = self.MinimaxDecision(gameState)

        return action
        
    def MinimaxDecision(self, gameState):

        currentDepth = 0

        minVals = []

        print gameState.getLegalActions(0)
        print self.depth
        
        for action in gameState.getLegalActions(0):
            minVals.append((self.MinValue(gameState.generateSuccessor(0,action), currentDepth, 1), action))

        print "minimax Decision: ",minVals

        maxC = -999999.0
        maxAction = None
        for pair in minVals:
            maxVal, action = pair
            if(maxVal > maxC):
                maxC = maxVal

                maxAction = action

        return maxAction
    


    def MinValue(self, gameState,currentDepth,currentGhost):
        
        cDepth = currentDepth

        '''
        if(self.depth == 1):
            print "last ghost"
            ghostMax = []
            
            for action in gameState.getLegalActions(currentGhost):
                
                ghostMax.append(self.MaxValue(gameState.generateSuccessor(currentGhost,action), cDepth))
                
            print "min val result: ",ghostMax
            print "min val depth: ",cDepth
            
            print "returning from minval"
            return min(ghostMax)
        '''

        if(cDepth == self.depth):     
                        
            return self.evaluationFunction(gameState)

        if not gameState.getLegalActions(currentGhost):
            return self.evaluationFunction(gameState)

        else:

            
            nGhosts = (gameState.getNumAgents())-1
            ghostMax = []
           # print currentGhost
           # print nGhosts

            if(currentGhost < nGhosts):

                for action in gameState.getLegalActions(currentGhost):
                
                    ghostMax.append(self.MinValue(gameState.generateSuccessor(currentGhost,action), cDepth,currentGhost+1))

              #  print "max min val result: ",ghostMax
              #  print "max val depth: ",cDepth

              #  print "returning from minval"
                return min(ghostMax)

            else:
                
                
               # print "last ghost"

                for action in gameState.getLegalActions(currentGhost):
            
                    ghostMax.append(self.MaxValue(gameState.generateSuccessor(currentGhost,action), cDepth+1))
                
                #print "min val result: ",ghostMax
                #print "min val depth: ",cDepth
                
               # print "returning from minval"
                return min(ghostMax)
            
        

    def MaxValue(self, gameState, currentDepth):

        cDepth = currentDepth

        #print "depth in  max value: ",cDepth

        if not gameState.getLegalActions(0):
            return self.evaluationFunction(gameState)

        if(cDepth == self.depth):
            
            return self.evaluationFunction(gameState)

        else:

            pacManActions = gameState.getLegalActions(0)
            pacManMinVals = []

            if(pacManActions):
                for action in pacManActions:
                    
                    pacManMinVals.append(self.MinValue(gameState.generateSuccessor(0,action), cDepth,1))
                    
                    ##print "returning from maxval"
                    
                #print "max val result: ",pacManMinVals
                #print "max val depth: ",cDepth
                    

                return max(pacManMinVals)
            else:
                #print "ugh getting here, ",pacManActions
                return 0
            


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

