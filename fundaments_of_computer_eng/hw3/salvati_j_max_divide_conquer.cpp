
#include <vector>
#include <iostream>
#include <cstdlib>
#include <random>
#include <assert.h>


using namespace std;
void populateVector ( vector< int > &A, double m);
void printVector ( vector< int > A);
int findMax ( vector< int > A, int x,int y);

int main (int argc, char* argv[]){
  int n;
  int m;

  cout << "specify length n: ";
  cin >> n;

  cout << "specify range [-m,m]: " ;
  cin >> m;

  vector<int> integers(n);
  populateVector(integers, m);
  int max = findMax(integers, 0, integers.size()-1);

  printVector(integers);
  cout << "findMax = " << max << endl;
  
  return 0;
}


int findMax ( vector< int > A, int x, int y){
  int val = -1;
  if(y-x<=1){
    return max(A[x],A[y]);
  }

  //not small enough problem yet, split
  val = (x+y)/2;
  int leftMax = findMax(A,x,val);
  int rightMax = findMax(A,val+1,y);

  return max(leftMax,rightMax);
}
    

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
