#include <vector>
#include <iostream>
#include <cstdlib>
#include <random>
#include <assert.h>

using namespace std;

void populateVector ( vector< int > &A, double m);
void printVector ( vector< int > A);

int intQuery ( vector< int > &A, int a, int b);


int main (int argc, char* argv[]){
  int n;
  int a;
  int b;
  int k;

  int result;

  cout << "specify length n: ";
  cin >> n;

  cout << "specify max int k:";
  cin >> k;

  cout << "specify range [a..b]" ;
  cin >> a;
  cin >> b;
  

  vector<int> integers(n);
  populateVector(integers, k);
  printVector(integers);

  result = intQuery( integers, a, b);
  
  cout << "total tally for a - b :";
  cout << result;
  cout << endl;
  

  return 0;
}


int intQuery  ( vector< int > &A, int a, int b){
  int i;
  int result = 0;

  //pre-process
  vector<int> table(A.size() + 1);

  for (i=0;i<A.size();i++){
    table[A[i]]++;   // increase count of each integer... 
  }

  //tally result
  for (i=a;i<=b;i++){
    result += table[i];  //total up ints in range a-b
  }

  return result;
}




void populateVector( vector< int > &A, double m){

  std::default_random_engine generator;
  std::uniform_int_distribution<int> distribution(0,m);

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
