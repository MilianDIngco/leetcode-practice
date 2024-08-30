import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class TimeMap {

    protected class Pair<K, V> {
        K one;
        V two;

        Pair(K one, V two) {
            this.one = one;
            this.two = two;
        }
    }

    HashMap<String, List<Pair<String, Integer>>> timeMap;

    public TimeMap() {
        timeMap = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        if (!timeMap.containsKey(key))
            timeMap.put(key, new ArrayList<>());
        timeMap.get(key).add(new Pair<String, Integer>(value, timestamp));
    }

    public String get(String key, int timestamp) {
        List<Pair<String, Integer>> times = timeMap.get(key);
        if (!timeMap.containsKey(key) || times.get(0).two > timestamp)
            return "";

        int l = 0, r = times.size() - 1, m = 0;

        while (l < r) {
            m = l + ((r - l) / 2);

            if (times.get(m).two < timestamp) {
                if (times.get(m + 1).two > timestamp) {
                    return times.get(m).one;
                }
                l = m + 1;
            } else if (times.get(m).two > timestamp) {
                r = m - 1;
            } else {
                return times.get(m).one;
            }

        }

        return times.get(r).one;
    }

    public static void main(String[] args) {
        TimeMap tm = new TimeMap() {
            {
                set("one", "two", 10);
                set("one", "three", 20);
                set("one", "five", 30);
            }
        };

        System.out.println(tm.get("one", 15));
        System.out.println(tm.get("one", 25));
        System.out.println(tm.get("one", 35));

    }
}
