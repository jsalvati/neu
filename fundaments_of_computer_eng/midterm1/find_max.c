#include <vector>
#include <iostream>
#include <cstdlib>
#include <random>
#include <assert.h>


using namespace std;
void populateVector ( vector< int > &A, double m);
void printVector ( vector< int > A);
int findMax ( vector< int > A, int y);

int calls = 0;

int main (int argc, char* argv[]){
  int n;
  int m;

  cout << "specify length n: ";
  cin >> n;

  cout << "specify range [-m,m]: " ;
  cin >> m;

  vector<int> integers(n);
  populateVector(integers, m);
  int max = findMax(integers, integers.size());

  printVector(integers);
  cout << "findMax = " << max << endl;
 
  cout << "findMax was called " << calls << " time(s)" << endl;
  
  return 0;
}


int findMax ( vector< int > A, int i){

  calls++;

  if ( i == 0){
    return A[0];
  }
  else 
    return max ( A[i],findMax( A ,  i-1));
}

  // if(i < A.size()){
  //  if(A[i] > max){
  //    max = A[i];
  //  }
  //  max = findMax(A, max, i+1);
  // }
   
  // return max;
//}
    
int max (int a, int b){
  if (a > b){
    return a;
  }else
    return b;
}

void populateVector( vector< int > &A, double m){

  std::default_random_engine generator;
  std::uniform_int_distribution<int> distribution(-m,m);

  for(int i=0;i<A.size();i++){
    int val = distribution(generator);
    A[i] = val;
  }
  return;
}

void printVector( vector< int > A ){

  for(int i=0;i < A.size(); i ++){
    cout << A[i] << ' ';
  }
  
  cout << endl;
  return;
}
