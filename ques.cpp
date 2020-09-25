#include <iostream>
#include <vector>
#include <string.h>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <list>

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
		else
			return false;
	}

	string getHint(string secret, string guess)
	{
		int a = 0, b = 0;
		vector<int> bullArray(10, 0), cowArray(10, 0);
		for (int i = 0; i < guess.size(); ++i)
		{
			if (secret[i] == guess[i])
				a += 1;
			else
			{
				bullArray[secret[i] - '0'] += 1;
				cowArray[guess[i] - '0'] += 1;
			}
		}
		for (int i = 0; i < 10; ++i)
		{
			b += min(bullArray[i], cowArray[i]);
		}
		return to_string(a) + 'A' + to_string(b) + 'B';
	}

	bool wordBreak(string s, vector<string> &wordDict)
	{
		unordered_set<string> dict(wordDict.cbegin(), wordDict.cend());
		return wordBreak(s, dict);
	}

	bool wordBreak(string &s, unordered_set<string> dict)
	{
		if (mem_.count(s))
			return mem_[s];
		if (dict.count(s))
			return mem_[s] = true;
		for (int i = 1; i < s.length(); ++i)
		{
			string left = s.substr(0, i);
			string right = s.substr(i);
			if (dict.count(right) && wordBreak(left, dict))
			{
				return mem_[s] = true;
			}
		}
		return mem_[s] = false;
	}

	bool isValid(string s)
	{
		stack<char> pa;
		for (int i = 0; i < s.size(); ++i)
		{
			if (s[i] == '(' || s[i] == '[' || s[i] == '{')
				pa.push(s[i]);
			else
			{
				if (pa.empty())
					return false;
				if (s[i] == ')' && pa.top() != '(')
					return false;
				if (s[i] == ']' && pa.top() != '[')
					return false;
				if (s[i] == '}' && pa.top() != '{')
					return false;
				pa.pop();
			}
		}
		return pa.empty();
	}

	vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
	{
		vector<int> res;
		unordered_map<int, int> tmp;
		for (int i = 0; i < nums1.size(); ++i)
		{
			if (tmp.find(nums1[i]) == tmp.end())
				tmp[nums1[i]] = 1;
		}
		for (int i = 0; i < nums2.size(); ++i)
		{
			auto addr = tmp.find(nums2[i]);
			if (addr != tmp.end() && addr->second == 1)
			{
				res.push_back(nums2[i]);
				addr->second = 2;
			}
		}
		return res;
	}

	vector<int> plusOne(vector<int> &digits)
	{
		int tmp = 0;
		for (int i = digits.size() - 1; i >= 0; --i)
		{
			if (digits[i] == 9)
			{
				tmp = 1;
				digits[i] = 0;
			}
			else
			{
				tmp = 0;
				digits[i]++;
				return digits;
			}
		}
		digits.insert(digits.begin(), 1);
		return digits;
	}

	bool isPossible(vector<int> &nums)
	{
		if (nums.size() < 3)
			return false;
		unordered_map<int, int> count;
		unordered_map<int, int> tail;
		for (int i = 0; i < nums.size(); ++i)
		{
			if (count.find(nums[i]) == count.end())
				count[nums[i]] = 1;
			else
				count[nums[i]]++;
		}
		for (int i = 0; i < nums.size(); ++i)
		{
			int tmp = nums[i];
			if (count[tmp] == 0)
				continue;
			else if (tail[tmp - 1] > 0)
			{
				count[tmp]--;
				tail[tmp - 1]--;
				tail[tmp]++;
			}
			else if (count[tmp + 1] > 0 && count[tmp + 2] > 0)
			{
				count[tmp]--;
				count[tmp + 1]--;
				count[tmp + 2]--;
				tail[tmp + 2]++;
			}
			else
			{
				return false;
			}
		}
		return true;
	}

	string decodeString(string s)
	{
		int i = 0;
		return decode(s, i);
	}

	string decode(string s, int &i)
	{
		string res = "";
		while (i < s.size() && s[i] != ']')
		{
			if (s[i] < '0' || s[i] > '9')
			{
				res += s[i++];
			}
			else
			{
				int count = 0;
				while (s[i] >= '0' && s[i] <= '9')
				{
					count = 10 * count + s[i++] - '0';
				}
				++i;
				string tmp = decode(s, i);
				++i;
				while (count > 0)
				{
					res += tmp;
					--count;
				}
			}
		}
		return res;
	}

	int helloworld() {
		cout << "hello, world\n";	//HAHA, this is just joking.
		return 0;
	} 


private:
	unordered_map<string, bool> mem_;
};

class NumArray
{
public:
	NumArray(vector<int> &nums)
	{
		stock = nums;
		for (int i = 1; i < nums.size(); ++i)
		{
			stock[i] += stock[i - 1];
		}
	}

	int sumRange(int i, int j)
	{
		return i == 0 ? stock[j] : stock[j] - stock[i - 1];
	}

private:
	vector<int> stock;
};

class LRUCache
{
public:
	LRUCache(int capacity) : cap(capacity) {}

	int get(int key)
	{
		if (keystock.find(key) == keystock.end())
			return -1;
		auto addr = keystock.find(key);
		stock.splice(stock.begin(), stock, addr->second);
		return addr->second->second;
	}

	void put(int key, int value)
	{
		auto addr = keystock.find(key);
		if (addr == keystock.end())
		{
			stock.push_front(make_pair(key, value));
			keystock[key] = stock.begin();
			if (stock.size() > cap)
			{
				int tmp = stock.rbegin()->first;
				stock.pop_back();
				keystock.erase(tmp);
			}
		}
		else
		{
			stock.erase(addr->second);
			stock.push_front(make_pair(key, value));
			keystock[key] = stock.begin();
		}
	}

private:
	int cap;
	list<pair<int, int>> stock;
	unordered_map<int, list<pair<int, int>>::iterator> keystock;
};

class Logger
{
public:
	Logger()
	{
	}

	bool shouldPrintMessage(int timestamp, string message)
	{
		if (printlog.find(message) == printlog.end())
		{
			printlog[message] = timestamp;
			return true;
		}
		else if (timestamp - printlog[message] >= 10)
		{
			printlog[message] = timestamp;
			return true;
		}
		else
		{
			return false;
		}
	}

private:
	unordered_map<string, int> printlog;
};

int main()
{
	printf("hello world");
	return 0;
}
