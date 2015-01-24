

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <memory>

using namespace std;

enum graph_type {
  invalid = 0,
  d = 1,
  und = 2
};

graph_type graphType = invalid;

class  Vertex {
 public:
  string name;   //only accept 1 letter names 
  char color;  
  int  d;
  int  pi;

 public:
  Vertex();
  Vertex(const string& n);
  
};

Vertex::Vertex (const string& n){
  name = n;
}

typedef vector< Vertex* > nodes;


//Read in a graph from given input file
void populateGraph (const string& fileName, vector< nodes > &G);
void determineGraphType (const string& type); 
void constructVertexes (const string& list, vector < nodes > &G);
void addEdges (const string& list, vector< nodes > &G);
nodes findNodeList(vector < nodes > &G, const string& node_name);
Vertex* findVertexPtr(vector < nodes > &G, const string& vertex_name);
