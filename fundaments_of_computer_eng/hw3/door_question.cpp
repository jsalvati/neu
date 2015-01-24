#include <vector>
#include <iostream>
#include <cstdlib> 

using namespace std;


int main(int argc, char* argv[]){
  
  cout << "starting program..." << endl;
  
  int n = atoi(argv[1]);
  int k = 0;
  int j = 0;
  int i = 0;
  u_int n_open = 0;

  cout << n << endl;
  
  vector<u_int> doors(n);

  for (i=0;i<n;i++){
    doors[i] = 0;
  }

  for(i=1;i<=n;i++){

    cout << "loop: " << i << " " << j <<  endl;

    for (k=j;k<n;k=k+i){
      if(doors[k] == 1){
	doors[k] = 0;
      }else{
	doors[k] = 1;
      }
    }

    j++;
  }
  
  cout << "door states: " << endl;

  for(i=0;i<n;i++){
    cout << doors[i];
    cout << " ";
    if(doors[i])
      n_open++;
  }


  cout << endl;
  cout << "Total open doors: " << n_open;
  

  
  return 0;
}
