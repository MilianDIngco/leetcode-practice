#include <iostream>
#include <string>
#include <unordered_map>
#include <queue>
#include <array>
using namespace std;

struct Node {
  string value;
  Node **children;
  int numChildren;
};

template<typename T>
bool inArray(T val, T arr[]) {
  int arrSize = *(&arr + 1) - arr;
  for(int i = 0; i < arrSize; i++) {
    if(arr[i] == val)
      return true;
  }
  
  return false;
}

string BFS(int current, Node * nodes[]) {
  int arrSize = *(&nodes + 1) - nodes;
  if(nodes[current]->numChildren == 0) {
    cout << "empty" << endl;
    return "";
  }
  string sol;

  int numAdded = 0;
  for(int i = 0; i < nodes[current]->numChildren; i++) {
    if( !inArray(nodes[current]->children[i], nodes ) ) {
      numAdded++;
      nodes[current + 1 + i] = nodes[current]->children[i];
      sol += nodes[current + 1 + i]->value;
    }
  }

  if(numAdded == 0 && current + 1 != arrSize - 1) {
    cout << "no mo kids" << endl;
    return "";
  } else {
    return sol + BFS(++current, nodes); 
  }

}

string BFS(Node * node, int numNodes) {
  Node ** nodes = new Node*[numNodes];
  nodes[0] = node;
  string sol = node->value + BFS(0, nodes);
  delete[] nodes;
  return sol;
}

int main (int argc, char *argv[])
{
  Node* one = new Node;
  one->value = "1";
  Node* two = new Node;
  two->value = "2";
  Node* three = new Node;
  three->value = "3";
  Node* four = new Node;
  four->value = "4";
  Node* five = new Node;
  five->value = "5";
  Node* six = new Node;
  six->value = "6";
  Node* seven = new Node;
  seven->value = "7";



  one->children = new Node*[2];
  one->children[0] = two;
  one->children[1] = three;
  one->numChildren = 2;
  two->children = new Node*[1];
  two->children[0] = one;
  two->numChildren = 1;
  three->children = new Node*[2];
  three->children[0] = one;
  three->children[1] = four;
  three->numChildren = 2;
  four->children = new Node*[2];
  four->children[0] = three;
  four->children[1] = five;
  four->numChildren = 2;
  five->children = new Node*[2];
  five->children[0] = six;
  five->children[1] = seven;
  five->numChildren = 2;
  six->children = new Node*[2];
  six->children[0] = five;
  six->children[1] = seven;
  six->numChildren = 2;
  seven->children = new Node*[2];
  seven->children[0] = five;
  seven->children[1] = six;
  seven->numChildren = 2;

  cout << BFS(one, 7);

  delete[] one->children;
  delete one;

  delete[] two->children;
  delete two;

  delete[] three->children;
  delete three;
 
  return 0;
}
