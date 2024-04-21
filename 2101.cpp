class Solution {
private:
    long long n;
    std::vector<std::vector<long long>> adj;

    bool inRange(std::vector<int>& bomb, std::vector<int>& target) {
        long long x = bomb[0], y = bomb[1], r = bomb[2];
        long long x1 = target[0], y1 = target[1];
        long long xx = (x1 - x) * (x1 - x);
        long long yy = (y1 - y) * (y1 - y);
        long long rr = static_cast<long long>(r) * r;
        return xx + yy <= rr;
    }

    void init(std::vector<std::vector<int>>& bombs) {
        n = bombs.size();
        adj.resize(n);
        for (long long i = 0; i < n; i++) {
            for (long long j = 0; j < n; j++) {
                if (j != i && inRange(bombs[i], bombs[j])) {
                    adj[i].push_back(j);
                }
            }
        }
    }

    void dfs(long long u, std::vector<bool>& visited) {
        if (visited[u]) return;
        visited[u] = true;
        for (long long v : adj[u]) {
            dfs(v, visited);
        }
    }

public:
    long long maximumDetonation(std::vector<std::vector<int>>& bombs) {
        init(bombs);
        long long best = 0;
        for (long long i = 0; i < n; i++) {
            long long cnt = 0;
            std::vector<bool> visited(n, false);
            dfs(i, visited);
            for (long long j = 0; j < n; j++) {
                if (visited[j]) {
                    cnt++;
                }
            }
            best = std::max(best, cnt);
        }
        return best;
    }
};
