class Solution {
public:
    /*
    use a map to hold count of nums

    fill map with values
    [8,8,8,9,9,6,6,6,6]
    {
        [8,3]
        [9,2]
        [6,4]
    }
    after filling this

    place all vectors {count, val}
    {3,1}
    {2,2}
    {4,3}
    sort this
    {2,2}
    {3,1}
    {4,3}

    iterate k=2
    look end of vector, grab the value and push it to the vector<int>
    find the 
    */
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> reverseFind;
        vector<int> mostFreq;
        
        //fill up unordered map with total counts of all unique values
        for(int i = 0; i < nums.size(); i++) {
            count[nums[i]]++;
        }
        
        //then we want to find the most counted values
        //place all values's count and value into a vector
        //then sort the vector based off the first value(count) in the vector's vector<int>
        for(auto it = count.begin(); it != count.end(); it++){
            reverseFind.push_back({it->second, it->first});
        }
        sort(reverseFind.begin(), reverseFind.end());
        //all counts sorted have highest counts at the back of vector
        for(int i = 0; i < k; i++){
            //reverseFind.back()[1] is the last value's value since [count, val]
            mostFreq.push_back(reverseFind.back()[1]);
            reverseFind.pop_back();
        }
        return mostFreq;
    }
};