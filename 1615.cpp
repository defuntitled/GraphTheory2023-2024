class Solution {
public:
    int maximalNetworkRank(int n, std::vector<std::vector<int>>& roads) {
        std::vector<std::vector<bool>> g(n, std::vector<bool>(n, false));
        
        for (auto& road : roads) {
            int x = road[0];
            int y = road[1];
            g[x][y] = g[y][x] = true;
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }

                int cur = 0;
                for (int k = 0; k < n; k++) {
                    if (k != i && k != j) {
                        if (g[i][k]) {
                            cur += 1;
                        }

                        if (g[j][k]) {
                            cur += 1;
                        }
                    }
                }

                if (g[i][j]) {
                    cur += 1;
                }

                ans = std::max(cur, ans);
            }
        }

        return ans;
    }
};
