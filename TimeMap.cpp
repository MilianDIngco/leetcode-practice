#include <string>
#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>

using Timeline = std::vector<std::pair<std::int, std::string>>;
using TimelineMap = std::unordered_map<std::string, timeline>;

class TimeMap{
  public:
    TimeMap() {}

    void setValue(std::string key, std::string value, int time) {
      if (tlm.find(key) == tlm.end()) {
        tlm[key] = {{time, value}};
      }
    }

    std::string getValue(std::string key, int time) {
      return "";
    }

  private:
    TimelineMap tlm;

    

    void resize()

}
