class Solution {
public:
    unordered_map<string,int> dict;

    string encode(vector<string>& strs) {
        string line;
        for(const auto& word: strs){
            line += word + ' ';
            dict[word]++;
        }
        return line;
    }

    /*
    n
    ne
    nee
    neet
    neet' , we need to add the char after, to not have reduncancy 
    */
    vector<string> decode(string s) {
        string word;
        vector<string> sum;
        for(char c : s){
            if(c == ' ' && dict[word]>0){
                sum.push_back(word);
                dict[word]--;
                word = "";
                continue;
            }
            word += c;
        }
        return sum;
    }
};


























// unordered_map<string, int> values;

//     string encode(vector<string>& strs) {
//         string output;
//         for(string s: strs){
//             values[s]++;
//             output += s + " ";
//         }
//         return output;
//     }

//     vector<string> decode(string s) {
//         vector<string> output;
//         string word;
//         for(char c: s){
//             if(c == ' ' && values[word]>0){
//                 output.push_back(word);
//                 values[word]--;
//                 word.clear();
//                 continue;
//             }
//             word += c;
//         }
//         return output;
//     }