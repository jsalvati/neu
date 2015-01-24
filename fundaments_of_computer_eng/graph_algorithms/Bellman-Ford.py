from graph import Graph

def InitSingleSource(G, s):
  #each vertex is handled implicitly when creating vertex objects
  s.d = 0

def Relax(u,v,w):
  if v.d > (u.d + w):
    v.d = u.d + w
    v.pi = u
 

def BellmanFord(G, s):  #w function is implicit in vertex implementation
  InitSingleSource(G,s)
  i = 1
  for i in range(i,len(G.vertList)-1):

    #graph is vertex oriented, get edges from each vertex (for each edge in E)
    for vertex in g:
      for edge in vertex.getConnections():
        Relax(vertex,edge,vertex.getWeight(edge))

  #graph is vertex oriented, get edges from each vertex (for each edge in E)
  for vertex in g:
    for edge in vertex.getConnections():
      if vertex.d > (edge.d + vertex.getWeight(edge)):
        return False

  return True

 


if __name__ == "__main__":
  g = Graph()
  g.populateExampleGraph()
  BellmanFord(g, g.getVertex(0))
  for v in g:
    print v
    if (not v.pi == None): 
      print "predessor: ", v.pi.id
    if (not v.f == "inf"): 
      print "finish: ", v.f
    
