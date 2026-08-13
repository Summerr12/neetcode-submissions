class Solution {
public:
    unordered_map<string, int> values;

    string encode(vector<string>& strs) {
        string output;
        for(string s: strs){
            values[s]++;
            output += s + " ";
        }
        return output;
    }

    vector<string> decode(string s) {
        vector<string> output;
        string word;
        for(char c: s){
            if(c == ' ' && values[word]>0){
                output.push_back(word);
                values[word]--;
                word.clear();
                continue;
            }
            word += c;
        }
        return output;
    }
};
