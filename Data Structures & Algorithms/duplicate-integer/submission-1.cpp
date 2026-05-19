#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> umap;
        for(int i =0; i <nums.size();i++){
            if (umap.count(nums[i]) == 0){
                umap[nums[i]]=1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};