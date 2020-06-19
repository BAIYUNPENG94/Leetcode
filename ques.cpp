#include <iostream>
#include <vector>
#include <string.h>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <stack>


using namespace std;

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(0), left(left), right(right) {}
};

class Solution
{
public:
	TreeNode *invertTree(TreeNode *root)
	{
		change(root);
		return root;
	}

	void change(TreeNode *dot)
	{
		if (dot != nullptr)
		{
			TreeNode *tmp;
			tmp = dot->left;
			dot->left = dot->right;
			dot->right = tmp;
			change(dot->left);
			change(dot->right);
		}
	}

	bool isValidBST(TreeNode *root)
	{
		return judgeTree(root, LONG_MIN, LONG_MAX);
	}

	bool judgeTree(TreeNode *dot, long min, long max)
	{
		if (dot == nullptr)
			return true;
		if (dot->left == nullptr && dot->right == nullptr)
			return true;
		bool con1 = (dot->right != nullptr) ? (dot->right->val > dot->val) && (dot->right->val < max) : true;
		bool con2 = (dot->left != nullptr) ? (dot->left->val < dot->val) && (dot->left->val > min) : true;
		if (con1 && con2)
		{
			return (judgeTree(dot->left, min, dot->val) && judgeTree(dot->right, dot->val, max));
		}
		else return false;
	}

	string getHint(string secret, string guess) {
		int a = 0, b = 0;		
		vector<int> bullArray (10, 0), cowArray(10, 0);
		for (int i = 0; i < guess.size(); ++i){
			if(secret[i] == guess[i]) a += 1;
			else{
				bullArray[secret[i] - '0'] += 1;
				cowArray[guess[i] - '0'] += 1;
			}
		}
		for (int i = 0; i < 10; ++i){
			b += min(bullArray[i], cowArray[i]);
		}
		return to_string(a) + 'A' + to_string(b) + 'B';
    }

	bool wordBreak(string s, vector<string>& wordDict) {
		unordered_set<string> dict(wordDict.cbegin(), wordDict.cend());
		return wordBreak(s, dict);
    }

	bool wordBreak(string& s, unordered_set<string> dict) {
		 if(mem_.count(s)) return mem_[s];
		 if(dict.count(s)) return mem_[s] = true;
		 for(int i = 1; i < s.length(); ++i){
			 string left = s.substr(0, i);
			 string right = s.substr(i);
			 if(dict.count(right) && wordBreak(left, dict)){
				 return mem_[s] = true;
			 }
		 }
		 return mem_[s] = false;
	}

	bool isValid(string s) {
		stack<char> pa;
		for (int i = 0; i < s.size(); ++i){
			if (s[i] == '(' || s[i] == '[' || s[i] == '{') pa.push(s[i]);
			else{
				if (pa.empty()) return false;
				if (s[i] == ')' && pa.top() != '(') return false;
				if (s[i] == ']' && pa.top() != '[') return false;
				if (s[i] == '}' && pa.top() != '{') return false;
				pa.pop();
			}
		}
		return pa.empty();
    }

	private:
		unordered_map<string, bool> mem_;

};

int main()
{
	printf("hello world");
	return 0;
}