class Solution {
public:
    bool isPalindrome(string s) {
        //kill punchuation, upper case and space
        string simplified;
        for(char c: s){
            if(!ispunct(c) && !isspace(c)){
                simplified += tolower(c);
            }
        }
        string simplified_r=simplified;
        reverse(simplified_r.begin(), simplified_r.end());
        if (simplified == simplified_r){
            return true;
        } 

        cout << simplified;
        return false;
    }
};