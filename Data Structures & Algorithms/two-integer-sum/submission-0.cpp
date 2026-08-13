class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> vals; //counting the count of each value
        int cur, remainder;
        vector<int> sol;
        for(int i=0; i<nums.size(); i++){
            cur = nums[i];
            remainder = target-cur;
            //check if remainder exists in map
            if(vals.find(remainder) != vals.end()){
                int sec_pos = vals.find(remainder)->second;
                if(i<sec_pos){
                    sol.push_back(i);
                    sol.push_back(sec_pos);
                }else{
                    sol.push_back(sec_pos);
                    sol.push_back(i);
                }

                return sol;
            }
            vals[cur] = i;
        }
        return sol;
    }
};
