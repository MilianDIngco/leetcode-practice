#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool isValid(string s) {
  if(s.empty()) return 0;
  
  stack<char> opens;

  for(int i = 0; i < s.length(); i++) {
    if(s[i] == '(' || s[i] == '[' || s[i] == '{')
      opens.push((s[i] == '(') ? ')' : (s[i] == '[') ? ']' : '}');
    if(s[i] == ')' || s[i] == ']' || s[i] == '}') {
      if(!opens.empty() && opens.top() == s[i]) 
        opens.pop();
      else
        return 0;
    }
  }

  return opens.empty();
}

int main (int argc, char *argv[]) {
  cout << isValid("[]({})");
  return 0;
}
