class Solution {
public:
    bool isPalindrome(int x) {
        string str1 = to_string(x);
        int len = str1.length();
        for (int i = 0; i < len/2; i++){
            if (str1[i] != str1[len-i-1])
                return false;
        }
        return true;
    }
};