#include <unordered_map>
#include <utility>
#include <vector>
#include <string>
#include <iostream>

using Timeline = std::vector<std::pair<int, std::string>>;
using TimelineMap = std::unordered_map<std::string, Timeline>;

class Test {
  public:
    TimelineMap tlm;

    Test() {}

    void setValue(std::string key, std::string value, int time) {
      if (tlm.find(key) == tlm.end()) {
        tlm[key] = {{time, value}};
      }
    }

    std::string getValue(std::string key, int time) {
      return "";
    }

    void printTimelineMap() {
      for(const auto& pair : tlm) {
        std::cout << pair.second[0].first << std::endl;
      }
    }

};

int main() {
  Test a;
  std::string key = "One";
  std::string value = "Value";
  int time = 5;
  a.setValue(key, value, time);
  a.printTimelineMap();
}

