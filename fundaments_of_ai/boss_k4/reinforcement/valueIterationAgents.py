# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
#from matplotlib.cbook import Null

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0


        #Initialize values counter
        """
        for state in mdp.getStates():
            if mdp.isTerminal(state):
                exit = mdp.getPossibleActions(state)
                
                self.values[state] = mdp.getReward(state, "") 
            else:
                self.values[state] = 0
        """

        #perform value iteration
        #self.values[state] = 
        #  max Sigma( T(s,a,nS) [ R(s,a,nS) + discount value(nS) ] )
        for i in range(0,iterations):
            
                    
            valuesCp = util.Counter()   
            
            for state in mdp.getStates():
                actionValues = []        
                
                if (mdp.getPossibleActions(state) and (not self.mdp.isTerminal(state))):
                
                    for action in mdp.getPossibleActions(state):
                        utility = self.getQValue(state, action)
                        actionValues.append(utility)
                    valuesCp[state] = max(actionValues)
                else:
                    valuesCp[state] = 0
                    
            
            self.values = valuesCp
                    
       


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
                    
        nStateProbPair = self.mdp.getTransitionStatesAndProbs(state,action)
        utility= 0
        for nStatePair in nStateProbPair: 
            nState,prob = nStatePair
            T = prob
            R = self.mdp.getReward(state,action,nState)
            utility += T*(R+self.discount*self.values[nState])
                    
        return utility
        

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """

        bestAction = None
        bestValue = -9999999  
        
        if((not self.mdp.isTerminal(state)) and self.mdp.getPossibleActions(state)):
        
            for action in self.mdp.getPossibleActions(state):  
                utility = self.getQValue(state, action)
                
                if utility >= bestValue:
                    bestAction  = action
                    bestValue = utility

 
        return bestAction
            

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
