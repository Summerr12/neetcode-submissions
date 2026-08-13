class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
        [2 * 3 * 4]
        [1 * 3 * 4]
        [1 * 2 * 4]
        [1 * 2 * 3]
        prefix
        suffix
        */
        int n = nums.size();
        vector<int> output(n,1);
        int rollingMult = 1;

        for(int i=0; i<n; i++){//left pass from left to right
            output[i] = rollingMult; 
            rollingMult *= nums[i];
        }
        
        rollingMult = 1;
        for(int j=n-1; j>=0; j--){//right pass from right to left
            output[j] *= rollingMult;
            rollingMult *= nums[j];
        }

        return output;
    }
};