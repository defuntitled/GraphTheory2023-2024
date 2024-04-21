class Solution {
public:
    using CycleException = std::runtime_error;

    void dfs(const int v,const int p, std::vector<int>& visited,
             std::unordered_map<int, std::vector<int> > &graph) const {
        visited[v] = 1;
        for (const auto u: graph[v]) {
            if (!visited[u]) {
                dfs(u,v, visited, graph);

            }else if(visited[u]==1){
                throw CycleException("lol");
            }
        }
        visited[v] = 2;
    }

    bool canFinish(int numCourses, std::vector<std::vector<int> > &prerequisites) {
        std::unordered_map<int, std::vector<int> > graph;
        for (const auto &rebr: prerequisites) {
            graph[rebr[1]].push_back(rebr[0]);
        }
        std::vector<int> visited(numCourses);
        try {
           for(auto v:graph){
               if(!visited[v.first]){
                   dfs(v.first,-1,visited,graph);
               }
           }
            return true;
        } catch (CycleException &e) {
            return false;
        }
    }
};
