#include <string>
#include <iostream>

using namespace std;

bool isPalindrome(string s) {
        string n = "";
        for(int i = 0; i < s.length(); i++) {
            if(s[i] <= 'Z' && s[i] >= 'A') {
                n += (s[i] + 32);
            } else if(s[i] <= 'z' && s[i] >= 'a') {
                n += (s[i]);
            }

        }
        std::cout << n << std::endl;
        if(n.length() < 2) {
            return true;
        } 
        for(int i = 0; i < n.length() / 2; i++) {
            if(n[i] != n[n.length() - i - 1]) {
                return false;
            }
        }

        return true;
    }

int main() {
  string s = "OP";
  if(isPalindrome(s)) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
