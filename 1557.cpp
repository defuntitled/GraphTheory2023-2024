class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        std::vector<int> visited(n,0);
        for(int i = 0; i<edges.size(); i++)
        {
            visited[edges[i][1]]++;
        }
        std::vector<int> ans;
        for(int i = 0; i < n; i++)
        {
            if(visited[i] == 0)
            {
                ans.push_back(i);
            }
                
        }
        return ans;
    }
};
