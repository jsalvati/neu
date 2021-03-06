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
            #print "food is adjacent!!"
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
             ((dx <= 1) and (dy <= 1)) )

    #print dx,dy
    

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
        self.alpha = None
        self.beta = None
        self.currentFoodCount = None
        self.lastFoodCount = None

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

        for action in gameState.getLegalActions(0):
            minVals.append((self.MinValue(gameState.generateSuccessor(0,action), currentDepth, 1), action))

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
        if(cDepth == self.depth):     
            return self.evaluationFunction(gameState)

        if not gameState.getLegalActions(currentGhost):
            return self.evaluationFunction(gameState)

        else:
            
            nGhosts = (gameState.getNumAgents())-1
            ghostMax = []

            if(currentGhost < nGhosts):

                for action in gameState.getLegalActions(currentGhost):
                
                    ghostMax.append(self.MinValue(gameState.generateSuccessor(currentGhost,action), \
                                                  cDepth,currentGhost+1))

                return min(ghostMax)

            else:

                for action in gameState.getLegalActions(currentGhost):
            
                    ghostMax.append(self.MaxValue(gameState.generateSuccessor(currentGhost,action), \
                                                  cDepth+1))
                return min(ghostMax)
            
        

    def MaxValue(self, gameState, currentDepth):

        cDepth = currentDepth

        if not gameState.getLegalActions(0):
            return self.evaluationFunction(gameState)

        if(cDepth == self.depth):
            
            return self.evaluationFunction(gameState)

        else:

            pacManActions = gameState.getLegalActions(0)
            pacManMinVals = []

            for action in pacManActions:
                
                pacManMinVals.append(self.MinValue(gameState.generateSuccessor(0,action), cDepth,1))  
                
            return max(pacManMinVals)




class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """


    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """

        action = self.MinimaxDecision(gameState)

        return action
        
    def MinimaxDecision(self, gameState):

        currentDepth = 0

        minVals = []
        alpha = -9999999
        beta = 9999999

        for action in gameState.getLegalActions(0):
            minVals.append((self.MinValue(gameState.generateSuccessor(0,action), currentDepth, 1,alpha,beta), action))
            
            alpha,action = max(alpha,max(minVals))

        maxC = -999999.0
        maxAction = None
        for pair in minVals:
            maxVal, action = pair
            if(maxVal > maxC):
                maxC = maxVal
                maxAction = action

        return maxAction
    

    def MinValue(self, gameState,currentDepth,currentGhost,alpha,beta):
        

        v = 99999999
        

        cDepth = currentDepth
        if(cDepth == self.depth):  
            return self.evaluationFunction(gameState)

        if not gameState.getLegalActions(currentGhost):
            return self.evaluationFunction(gameState)

        else:
            
            nGhosts = (gameState.getNumAgents())-1
            ghostMax = []
           

            for action in gameState.getLegalActions(currentGhost):
                if(currentGhost < nGhosts):
                    v = min(v,self.MinValue(gameState.generateSuccessor(currentGhost,action), \
                                            cDepth,currentGhost+1,alpha,beta))
                else:
                    v = min(v,self.MaxValue(gameState.generateSuccessor(currentGhost,action), \
                                                  cDepth+1,alpha,beta))
                    
                if v < alpha:
            
                    return v
                    
                beta = min(beta,v)
                
            return v
            
        

    def MaxValue(self, gameState, currentDepth, alpha, beta):

        cDepth = currentDepth

        if not gameState.getLegalActions(0):
            return self.evaluationFunction(gameState)

        if(cDepth == self.depth):
            return self.evaluationFunction(gameState)

        else:

            pacManActions = gameState.getLegalActions(0)
            pacManMinVals = []

            for action in pacManActions:
                
                pacManMinVals.append(self.MinValue(gameState.generateSuccessor(0,action), cDepth,1,alpha,beta))  

                #print "current max; ",max(pacManMinVals)
                #print "beta: ",self.beta
  
                if (beta != None):
                    if max(pacManMinVals) > beta:
                        #print "rejecting self.beta"
                        return max(pacManMinVals)

                
                alpha = max(alpha,max(pacManMinVals))
                #rint "alpha: ",self.alpha

            return max(pacManMinVals)



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """


    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """

        action = self.MinimaxDecision(gameState)

        return action
        
    def MinimaxDecision(self, gameState):

        currentDepth = 0

        minVals = []

        for action in gameState.getLegalActions(0):
            minVals.append((self.ExpectValue(gameState.generateSuccessor(0,action), currentDepth, 1), action))
 

        maxC = -999999.0
        maxAction = None
        for pair in minVals:
            maxVal, action = pair
            if(maxVal > maxC):
                maxC = maxVal
                maxAction = action

        return maxAction
    

    def ExpectValue(self, gameState,currentDepth,currentGhost):
        
        v = 0
        cDepth = currentDepth
        if(cDepth == self.depth):  
            return self.evaluationFunction(gameState)

        if not gameState.getLegalActions(currentGhost):
            return self.evaluationFunction(gameState)

        else:
            
            nGhosts = (gameState.getNumAgents())-1
        
            prob = (1.0/len(gameState.getLegalActions(currentGhost)))

            for action in gameState.getLegalActions(currentGhost):
                

                if(currentGhost < nGhosts):
                    
                    v += prob*(self.ExpectValue(gameState.generateSuccessor(currentGhost,action), \
                                            cDepth,currentGhost+1))
                else:
                    v += prob*(self.MaxValue(gameState.generateSuccessor(currentGhost,action), \
                                                  cDepth+1))
                
            return v
            
        

    def MaxValue(self, gameState, currentDepth):

        cDepth = currentDepth

        if not gameState.getLegalActions(0):
            return self.evaluationFunction(gameState)

        if(cDepth == self.depth):
            return self.evaluationFunction(gameState)

        else:

            pacManActions = gameState.getLegalActions(0)
            pacManMinVals = []

            for action in pacManActions:
                
                pacManMinVals.append(self.ExpectValue(gameState.generateSuccessor(0,action), cDepth,1))  


            return max(pacManMinVals)



def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

    """
    currentPosition = currentGameState.getPacmanPosition()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    food = currentGameState.getFood()
    foodCount = len(food.asList())    
    

    score = 99999999
    
    foodDistance = findDistanceToClosestDot(currentGameState)
    
    capsuleDistance = findDistanceToClosestCapsule(currentGameState)

    if(foodCount > 0):
        score -= foodDistance*4

    if currentPosition == betterEvaluationFunction.lastPosition:
        score -= 100000
 
    for ghost in newGhostStates:

        ghostDistance = util.manhattanDistance(currentPosition, ghost.getPosition())

        if((newScaredTimes[0] == 0) and (ghostDistance < 14)):

            
            if(ghostDistance):
                score -= ((1.0/ghostDistance))*200
            else:
                score -= 100000000
        else:
            if(ghostDistance):
                score -= (ghostDistance**2)*200
            else: 
                score += 10000000000

    
    if currentGameState.isWin():
        score += 1000000

    if (foodCount > 0):
        score -= foodCount*1000


    betterEvaluationFunction.lastPosition = currentPosition
    
    return score
    

    

def findDistanceToClosestDot(gameState):
    """
    Returns a path (a list of actions) to the closest dot, starting from
    gameState.
    """
    # Here are some useful elements of the startState
    startPosition = gameState.getPacmanPosition()
    food = gameState.getFood()
    foodList = food.asList()
    
    closestFood = None
    maxDistance = 0
    for food in foodList:
        if closestFood == None:
            closestFood = food
            maxDistance = util.manhattanDistance(startPosition,food)
        else:
            distance = util.manhattanDistance(startPosition,food)
            if (distance > maxDistance):
                closestFood = food
                maxDistance = distance
                    
    return maxDistance

def findDistanceToClosestCapsule(gameState):
    """
    Returns a path (a list of actions) to the closest dot, starting from
    gameState.
    """
    # Here are some useful elements of the startState
    startPosition = gameState.getPacmanPosition()
    foodList = gameState.getCapsules()
    
    closestFood = None
    maxDistance = 999999999
    for food in foodList:
        if closestFood == None:
            closestFood = food
            maxDistance = util.manhattanDistance(startPosition,food)
        else:
            distance = util.manhattanDistance(startPosition,food)
            if (distance < maxDistance):
                closestFood = food
                maxDistance = distance
                    
    return maxDistance

# Abbreviation
better = betterEvaluationFunction



    
betterEvaluationFunction.lastPosition = 0
    
