class Solution {
public:
    void dfs(std::vector<int>& keys, std::vector<bool>& visited,std::vector<vector<int>>& rooms){
        for(auto key : keys) {
            if(visited[key]) {
                continue; 
            }
            visited[key] = true;
            dfs(rooms[key],visited,rooms);
        }
    }
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
    vector<bool> visited(rooms.size(), false);
    std::vector<int> start = {0};
    dfs(start,visited,rooms); 
    if(std::count(visited.begin(),visited.end(),false)){
        return false;
    }
    return true;
    }
};
