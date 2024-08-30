#include <string>
#include <vector>
#include <iostream>
using namespace std;

string lcp(vector<string>& strs) {

  string sol;
  int minLen = strs.at(0).length();
  
  for(int i = 0; i < strs.size(); i++) {
    if(strs[i].length() < minLen) 
      minLen = strs[i].length();
  }

  for(int i = 0; i < minLen; i++) {
    char current = strs.at(0)[i];
    for(int j = 0; j < strs.size(); j++) {
      if(strs.at(j)[i] != current) {
        goto finished;
      }
    }
    sol += string(1, current);
  }
  finished:
    return sol;
} 

int main (int argc, char *argv[])
{
  vector<string> * strs = new vector<string>;
  strs->push_back("");
  strs->push_back("");
  strs->push_back("");
  cout << lcp(*strs);

  delete strs;
  return 0;
}
