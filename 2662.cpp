class Solution {
    
    struct Pair {
        int x;
        int y;
        int cost;
        Pair(int x, int y, int cost) : x(x), y(y), cost(cost) {}
    };

public:
    int minimumCost(std::vector<int>& start, std::vector<int>& target, std::vector<std::vector<int>>& specialRoads) {
        int m = specialRoads.size();
        int n = specialRoads[0].size();
        std::unordered_map<int, std::unordered_set<int>> map;
        
        std::priority_queue<Pair, std::vector<Pair>, std::function<bool(Pair, Pair)>> pq([](Pair a, Pair b) { return a.cost > b.cost; });
        
        int fx = target[0];
        int fy = target[1];
        int x1 = start[0];
        int y1 = start[1];
        
        pq.push(Pair(x1, y1, 0));
        
        while (!pq.empty()) {
            Pair rem = pq.top();
            pq.pop();
            x1 = rem.x;
            y1 = rem.y;
            
            if (map.count(x1) && map[x1].count(y1)) {
                continue;
            }
            
            if (!map.count(x1)) {
                map[x1] = std::unordered_set<int>();
            }
            map[x1].insert(y1);
            
            if (rem.x == fx && rem.y == fy) {
                return rem.cost;
            }
            
            pq.push(Pair(fx, fy, rem.cost + std::abs(x1 - fx) + std::abs(y1 - fy)));
            
            for (int i = 0; i < specialRoads.size(); i++) {
                int x = specialRoads[i][0];
                int y = specialRoads[i][1];
                int x2 = specialRoads[i][2];
                int y2 = specialRoads[i][3];
                int ct = specialRoads[i][4];
                
                if (map.count(x2) && map[x2].count(y2)) {
                    continue;
                }
                pq.push(Pair(x2, y2, rem.cost + ct + std::abs(x1 - x) + std::abs(y1 - y)));
            }
        }
        
        return -1;
    }
};
