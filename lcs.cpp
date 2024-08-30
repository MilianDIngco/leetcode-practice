#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
  public:
    int longestConsecutiveSequence(std::vector<int>& nums) {
      std::unordered_map<int, int> hm;
      int max = -1;
      for(int i = 0; i < nums.size(); i++) {
        std::cout << "Current: " << nums.at(i) << std::endl;
        if(hm.find(nums.at(i) - 1) != hm.end()) {
          hm[nums.at(i) - 1]++;
          hm[nums.at(i)] = hm[nums.at(i) - 1];
          hm.erase(nums.at(i) - 1);
        } else {
          hm[nums.at(i)] = 1;
        }
        max = (max < hm[nums.at(i)]) ? hm[nums.at(i)] : max;
        std::cout << "---------------" << std::endl;
        std::cout << "max: " << max << std::endl;

        for(auto it = hm.begin(); it != hm.end(); it++) {
          std::cout << it->first << ": " << it->second << std::endl;
        }
        std::cout << "---------------" << std::endl;

      }
      return max;
    }
};

int main() {
  Solution a;
  std::vector<int> nums = {0,3,2,5,4,6,1,1};
  int length = a.longestConsecutiveSequence(nums);
  std::cout << length << std::endl;
}
