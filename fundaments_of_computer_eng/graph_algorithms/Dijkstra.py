from graph import Graph
from priorityQueue import PriorityQueue


def InitSingleSource(G, s):
  #each vertex is handled implicitly when creating vertex objects
  s.d = 0

def Relax(u,v,w):
  if v.d > (u.d + w):
    v.d = u.d + w
    v.pi = u
 

def Dijkstra(G, s):  #w function is implicit in vertex implementation
    
  InitSingleSource(G,s)
  pq = PriorityQueue()
  pq.buildHeap([(v.d,v) for v in G])

  while not pq.isEmpty():
    u = pq.delMin()
    for v in u.getConnections():
      Relax(u,v,u.getWeight(v))
      pq.decreaseKey(v, v.d)

  return True

 


if __name__ == "__main__":
  g = Graph()
  g.populateExampleGraph()
  Dijkstra(g, g.getVertex(0))
  for v in g:
    print v
    if (not v.pi == None): 
      print "predessor: ", v.pi.id
    if (not v.f == "inf"): 
      print "finish: ", v.f
    
