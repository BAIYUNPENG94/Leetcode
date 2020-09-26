#include <iostream>
#include <vector>
#include <string.h>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <list>

using namespace std;

class Solution{
    string largestNumber(vector<int>& nums){
        vector<string> arr;
        for(auto i:nums){
            arr.push_back(to_string(i));
        }
        sort(begin(arr), end(arr), [](string& s1, string& s2){return s1+s2 > s2+s1;});
        string res;
        for(auto s:arr){
            res += s;
        }
        while(res[0] == '0' && res.length() > 1){
            res.erase(0, 1);
        }
        return res;
    }

    bool isPalindrome(int x){
        if(x < 0){
            return false;
        }
        long temp = x, rev = 0;
        do{
            rev = rev * 10 + x % 10;
            x = x / 10;
        }while(x != 0);
        if(rev == temp){
            return true;
        }
        else{
            return false;
        }
    }

    int maxArea(vector<int>& height){
        int ans = 0, l = 0, r = height.size() - 1, area = 0;
        while(l < r){
            area = (r - l) * (min(height[l], height[r]));
            if(area > ans){
                ans = area;
            }
            if(height[l] < height[r]){
                ++l;
            }
            else{
                --r;
            }
        }
        return ans;
    }

    string intToRoman(int num){
        string res = "";
        string roman_as[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int roman_vals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        for(int i = 0; i < 13; ++i){
            while(num - roman_vals[i] >= 0 ){
                res += roman_as[i];
                num -= roman_vals[i];
            }
        }
        return res;
    }

    int findPoisonedDuration(vector<int>& timeSeries, int duration){
        int temp = 0, res = 0;
        for(int i = 0; i < timeSeries.size(); ++i){
            if(temp == 0){
                res += duration;
            }
            else{
                if(timeSeries[i] - temp < duration){
                    res += timeSeries[i] - temp;
                }
                else{
                    res += duration;
                }
            }
            temp = timeSeries[i];
        }
        return res;
    }

    int findPoisonedDuration(vector<int>& timeSeries, int duration){
        if(timeSeries.empty()) return 0;
        int res = duration;
        for(int i = 1; i < timeSeries.size(); ++i){
            if(timeSeries[i] - timeSeries[i-1] > duration) res += duration;
            else res += timeSeries[i] - timeSeries[i-1];
        }
        return res;
    }
};