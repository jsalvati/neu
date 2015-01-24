
from graph import Graph
import DFS


if __name__ == "__main__":
    g = Graph()
    g.populateExampleGraph()

    topSort = DFS (g)

    
    for v in g:
      print v
      if (not v.pi == None):
       print "predessor: ", v.pi.id
      if (not v.f == "inf"):
       print "finish: ", v.f
    
    for v in topSort:
     print " ",v.f
    
