from graph import Graph
from queue import Queue



def BFS (G, S):
  S.color = "Gray"
  S.d = 0
  S.pi = None
  Q = Queue()
  Q.enqueue(S)
  while (not Q.isEmpty()):
    u = Q.dequeue()
    for v in u.getConnections():
      if (v.color == "White"):
        v.color = "Gray"
        v.d = u.d+1
        v.pi = u
        Q.enqueue(v)
    u.color = "Black"


if __name__ == "__main__":
    g = Graph()
    g.populateExampleGraph()
    BFS (g, g.getVertex(0))
    for v in g:
      print v
      if (not v.pi == None):
       print "predessor: ", v.pi.id
    
