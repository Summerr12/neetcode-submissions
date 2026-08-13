class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> sol;
        unordered_map<string,vector<string>> cleanedWords;
        //<cleaned word, word>
        string cleanedWord;
        for(int i=0; i<strs.size(); i++) {
            cleanedWord = strs[i];
            sort(cleanedWord.begin(), cleanedWord.end());
            cleanedWords[cleanedWord].push_back(strs[i]);
        }
        for(auto const& pairs: cleanedWords){
            sol.push_back(pairs.second);
        }
        return sol;
    }
};
