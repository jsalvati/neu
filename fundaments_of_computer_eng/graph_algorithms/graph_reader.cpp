
#include "graph_reader.h"


//Read in a graph from given input file
void populateGraph (const string& fileName, vector< nodes > &G){
  string line;

  ifstream input_graph (fileName);
  if(input_graph.is_open()){
   
    //determine graph type
    getline(input_graph, line);
    determineGraphType(line);

    //construct list of vectors
    getline(input_graph,line);
    constructVertexes(line, G);

    //generateEdges
    while(getline(input_graph,line)){
      addEdges(line, G);
    }

  }
  else{
    cout << "unable to open file \n";
    return;
  }
}


void determineGraphType (const string& line){
  
  string directed = "directed";
  string undirected = "undirected";

  if(line.compare(directed)){
    cout << "directed graph\n";
    graphType = d;
  }
  else if(line.compare(undirected)){
    cout << "undirected graph\n";
    graphType = und;
  }else {
    cout << "invalid graph type\n";
  }
  return;
}


void constructVertexes(const string& list, vector< nodes > &G){
  string vertex_delimiter = ",";
  size_t start = 0;
  size_t end = list.find(vertex_delimiter,start);
  string token;

  nodes V;
  Vertex* vertex;
  int i = 0;

  while (end != string::npos){
    token = list.substr(start,end-start);
    cout << token << endl;
    
   
    vertex = new Vertex(token);
    V.push_back(vertex);
    cout << "adding vertex: " << V[0]->name << endl;
    G.push_back(V);
    start = end + vertex_delimiter.length();
    end = list.find(vertex_delimiter, start);
    V.clear();
    
  }

  return; 
}

void addEdges (const string& list, vector< nodes > &G){
  string node_edge_delimiter = ">";
  string vertex_delimiter = ",";
  size_t start = 0;
  string token;

  Vertex* v;
  nodes n;
  
  // detemine node we are adding edges to
  size_t end = list.find(node_edge_delimiter,start);
  if(end == string::npos){
    //cout << "node has no edges" << endl;
    return;
  }

  token = list.substr(start,end-start);
  //cout << "node token: " <<token << endl;
  n = findNodeList(G, token);
  start = end + node_edge_delimiter.length();

  end = list.find(vertex_delimiter, start);

  // iterate through node list to add edges
  while (end != string::npos){
    token = list.substr(start,end-start);
    //cout << "edge token: " <<token << endl;

    v = findVertexPtr(G,token);
    n.push_back(v);
    start = end + vertex_delimiter.length();
    end = list.find(vertex_delimiter, start);
  }
}

nodes findNodeList(vector < nodes > &G, const string& node_name){
  int i;
  nodes tempNodes;
  

  for (i=0;i<(G.size());i++){
    tempNodes = G[i];
    string n = tempNodes[0]->name;
    //cout << "find node list: " << node_name << endl;
    //cout << "tempNodes: " << tempNodes[0]->name << endl;
    if (!n.compare(node_name)){
      //cout << "find node list successful" << endl;
      return tempNodes;
    }
  }

  //cout<< "no matching node in list for node: " << node_name << endl;
  return tempNodes;
}

Vertex* findVertexPtr(vector < nodes > &G, const string& vertex_name){
  int i;
  nodes n;
  Vertex* vertex;
  

  for (i=0;i<(G.size());i++){
    n = G[i];
    if (!n[0]->name.compare(vertex_name)){
      return vertex;
    }
  }

  //cout<< "no matching edge in list for edge:" << vertex_name << endl;
  return vertex;
}

int main (){

  vector< nodes > G;
  string filename = "directed_graph1.txt";

  populateGraph(filename, G);

  return 0;
}
