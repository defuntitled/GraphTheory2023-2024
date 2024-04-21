class Solution {
public:
     int n;
     int m;
    
     int helper(std::vector<std::vector<int>>& arr) {
        std::vector<std::vector<int>> dist(n, std::vector<int>(m, 1<<30));
        
        std::deque<std::vector<int>> dq;
        
        dq.push_front({0, 0});
        dist[0][0] = 0;

        std::vector<int> dx = {0, 0, 1, -1};
        std::vector<int> dy = {1, -1, 0, 0};

        while (!dq.empty()) {
            auto a = dq.front();
            dq.pop_front();
            int x = a[0];
            int y = a[1];

            int dir = arr[x][y];

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                int wt = 1;
                if (k + 1 == dir) wt = 0;
                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    if (dist[nx][ny] > dist[x][y] + wt) {
                        dist[nx][ny] = dist[x][y] + wt;
                        if (wt == 1) dq.push_back({nx, ny});
                        else dq.push_front({nx, ny});
                    }
                }
            }
        }
        
        return dist[n - 1][m - 1];
    }
    
    int minCost(std::vector<std::vector<int>>& arr) {
        n = arr.size();
        m = arr[0].size();
        return helper(arr);
    }
};
