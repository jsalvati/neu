
from graph import Graph

time = 0
topSort = []

def DFS_visit(vertex):
  global time
  global topSort
  time = time+1
  vertex.d = time
  vertex.color = "Gray"
  for v in vertex.getConnections():
    if (v.color == "White"):
      DFS_visit(v)
  vertex.color = "Black"
  time = time+1
  vertex.f = time
  #for topological sorting, sort vertices into topSort based on finish times
  topSort.insert(0,vertex)

def DFS (G):
  global time
  time = 0
  for v in g:
    if (v.color == "White"):
      DFS_visit(v)

  return topSort



if __name__ == "__main__":
    g = Graph()
    g.populateExampleGraph()
    DFS (g)
    for v in g:
      print v
      if (not v.pi == None):
       print "predessor: ", v.pi.id
      if (not v.f == "inf"):
       print "finish: ", v.f
    
    for v in topSort:
     print " ",v.f
    
