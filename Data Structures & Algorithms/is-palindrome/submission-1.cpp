class Solution {
public:
    bool isPalindrome(string s) {
        string simple;
        for(char c: s){
            if(!ispunct(c) && !isspace(c)){
                simple += tolower(c);
            }
        }
        int endCount = simple.length()-1;
        for(int i = 0 ; i < simple.length(); i++){
            if(simple[i] != simple[endCount]){
                return false;
            }
            endCount--;
        }
        return true;
    }
};
