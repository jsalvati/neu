#include "insertion_sort.h"


//using namespace std
int main(){
  int n;
  int m;

  cout << "specify length n: ";
  cin >> n;

  cout << "specify range [-m,m]: " ;
  cin >> m;

  vector<int> integers(n);

  populateVector(integers, m);
  insertionSort(integers);
  printVector(integers);
  
  for (int i=0;i<integers.size()-1;i++){
    //assert correctness of insertion sort
    assert(integers[i] <= integers[i+1]);
  }

  cout << "insertion is in order as per the assertion integers[i] <= integers[i+1] for all elements" << endl;

  return 0;
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

void insertionSort( vector< int > &A ){

  int key;
  int i;

  for(int j=1; j<A.size();j++){
    key = A[j];
    i = j-1;
    while ( (i >= 0) && (A[i] > key)){
      A[i+1] = A[i];
      i = i-1;
    }
    A[i+1] = key;

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
