#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
  public:
    int longestConsecutiveSequence(std::vector<int>& nums) {
      std::unordered_map<int, int> hm;
      std::vector<std::string> combined;
      int group = 0;
      int rearranged = 0;
      for(int i = 0; i < nums.size(); i++) {
        //if map doesn't contain it, or any around it, add it under a new group
        if(hm.find(nums.at(i)) == hm.end() && hm.find(nums.at(i) + 1) == hm.end() && hm.find(nums.at(i) - 1) == hm.end()) {
          hm[nums.at(i)] = group++; 
        //found both
        } else if(hm.find(nums.at(i) - 1) != hm.end() && hm.find(nums.at(i) + 1) != hm.end() && hm[nums.at(i) - 1] != hm[nums.at(i) + 1]) {
          //iterate through map and change hm[+1] to hm[-1]
          int group1 = hm[nums.at(i) - 1];
          int group2 = hm[nums.at(i) + 1];

          hm[nums.at(i)] = group1;
          combined.push_back(std::to_string(group1) + std::to_string(group2));
          /*for(auto it = hm.begin(); it != hm.end(); it++) {
            if(it->second == group2) {
              hm[it->first] = group1;
            }
          }*/
          rearranged++;
        //found -1
        } else if(hm.find(nums.at(i) - 1) != hm.end()) {
          hm[nums.at(i)] = hm[nums.at(i) - 1];
        //found +1
        } else if(hm.find(nums.at(i) + 1) != hm.end()) {
          hm[nums.at(i)] = hm[nums.at(i) + 1];
        } 
      }
      
      std::vector<int> count(group);
      for(auto it = hm.begin(); it != hm.end(); it++) {
        std::cout << it->first << ": " << it->second << std::endl;
        count.at(it->second)++;
      }
      
      for(int i : count) {
        std::cout << i << " ";
      }
      std::cout << std::endl;

      for(int i = 0; i < combined.size(); i++) {
        std::cout << combined.at(i) << std::endl;
        for(int n = 1; n < combined.at(i).length(); n++) {
          count.at(combined.at(i)[0] - '0') += count.at(combined.at(i)[n] - '0');
          count.at(combined.at(i)[n] - '0') = 0;
        }
      }

      int max = 0;
      for(int i = 0; i < count.size(); i++) {
        max = (max < count.at(i)) ? count.at(i) : max;
      }
      
      std::cout << "rearranged: " << rearranged << std::endl;

      return max;
    }
};

int main() {
  Solution a;
  std::vector<int> nums = {0,3,7,2,5,8,4,6,0,1};
  int lcs = a.longestConsecutiveSequence(nums);
  std::cout << "LCS: " << lcs << std::endl;
}
