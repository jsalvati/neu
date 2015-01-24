#include <iostream>
#include <vector>
#include <cstdlib>
#include <random>
#include <assert.h>

using namespace std;


int total_count = 0;

void rankA( int A[], int n, int i);
void populateVector ( vector< int > &A, double m);
void printVector ( vector< int > A);

int main(int argc, char* argv[]){

  

  int B[5] = {2, 3, 4, 5 ,6};
  
  int i;

  for (i=0;i<5;i++){
    cout << B[i] << " ";
  }
  cout << endl;

  rankA(B, 4, 0);
  
  for (i=0;i<5;i++){
    cout << B[i] << " ";
  }
  cout << endl;
  
  // printVector (rank_test);
  
  cout << total_count << endl;

  return 0;
}


void rankA( int A[], int n, int i){

  total_count++;
  if (i < n){
    rankA(A, n, i+1);
    A[i] += A[i+1]; 
  }

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

}
