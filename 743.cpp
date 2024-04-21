class Solution {
public:

    const int int_max = 1<<30;
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        std::vector<std::vector<int>> cost(n + 1, std::vector<int>(n + 1, int_max >> 1));
    
    for(int i = 1; i <= n; i++){
        cost[i][i] = 0;
    }

    for(int i = 0; i < times.size(); i++){
        cost[times[i][0]][times[i][1]] = times[i][2];
    }

    for(int k = 1; k <= n; k++){
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                cost[i][j] = std::min(cost[i][j], cost[i][k] + cost[k][j]);
            }
        }
    }

    int res = 0;
    for(int i = 1; i <= n; i++){
        if(cost[k][i] > 6000) return -1;
        res = std::max(res, cost[k][i]);
    }
    return res;
    }
};
