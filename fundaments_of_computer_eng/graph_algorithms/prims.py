
import sys
from graph import Graph
from priorityQueue import PriorityQueue


def PrimsMST(G, s):
  s.d = 0
  pq = PriorityQueue()
  pq.buildHeap([(v.d,v) for v in G])

  while not pq.isEmpty():
    v = pq.delMin()
    for edgeV in v.getConnections():
      if (edgeV in pq) and (v.getWeight(edgeV) <  edgeV.d):
        edgeV.pi = v
        edgeV.d = v.getWeight(edgeV)
        pq.decreaseKey(edgeV,edgeV.d)
  

if __name__ == "__main__":
    g = Graph()
    g.populateExampleGraph()
    PrimsMST(g,g.getVertex(0))
    for v in g:
      print v
      if (not v.pi == None):
       print "predessor: ", v.pi.id
      if (not v.f == sys.maxsize):
       print "finish: ", v.f

