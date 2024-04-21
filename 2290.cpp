class Solution {
public:
    int minimumObstacles(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        std::vector<std::vector<int>> distance(m, std::vector<int>(n, 1<<30));
        distance[0][0] = 0;
        
        std::deque<std::vector<int>> q;
        q.push_back({0, 0, 0});
        
        while (!q.empty()) {
            auto fr = q.front();
            int d = fr[0];
            int i = fr[1];
            int j = fr[2];
            q.pop_front();
            
            if (i == m - 1 && j == n - 1) {
                return d;
            }

            std::vector<std::vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            for (const auto&  direction : directions) {
                int di = direction[0];
                int dj = direction[1];
                int ci = i + di;
                int cj = j + dj;
                if (ci >= 0 && ci < m && cj >= 0 && cj < n) {
                    if (d + grid[ci][cj] < distance[ci][cj]) {
                        distance[ci][cj] = d + grid[ci][cj];
                        if (grid[ci][cj] == 1) {
                            q.push_back({distance[ci][cj], ci, cj});
                        } else {
                            q.push_front({distance[ci][cj], ci, cj});
                        }
                    }
                }
            }
        }
        
        return distance[m - 1][n - 1];
    }
};
