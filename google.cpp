#include <iostream>
#include <vector>
#include <string.h>
#include <sstream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class StringIterator
{
private:
    string str;
    int index;
    char cur;
    int count;

public:
    StringIterator(string compressedString)
    {
        str = compressedString;
        index = 0;
        cur = ' ';
        count = 0;
    }

    char next()
    {
        if (!hasNext())
        {
            return ' ';
        }
        if (count != 0)
        {
            count--;
            return cur;
        }
        cur = str[index];
        index++;
        while (str[index] >= '0' && str[index] <= '9')
        {
            count = 10 * count + str[index] - '0';
            index++;
        }
        count--;
        return cur;
    }

    bool hasNext()
    {
        return index < str.size() || count != 0;
    }
};

class Solution
{
    //NULL means empty pointer.
public:
    ListNode *reverseList(ListNode *head)
    {
        if (head == NULL)
            return NULL;
        ListNode *start = head;
        ListNode *prev = NULL;
        ListNode *next = NULL;
        ListNode *curr = head;
        while (curr != NULL)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
        return head;
    }

    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.empty())
            return "";
        string result = "";
        for (int i = 0; i < strs[0].size(); ++i)
        {
            char c = strs[0][i];
            for (int j = 0; j < strs.size(); ++j)
            {
                if (i >= strs[j].size() || c != strs[j][i])
                {
                    return result;
                }
            }
            result.push_back(c);
        }
        return result;
    }

    bool isSubsequence(string s, string t)
    {
        bool answer = true;
        int position;
        for (int i = 0; i < s.length(); ++i)
        {
            position = t.find(s[i]);
            if (position != s.npos)
            {
                t = t.substr(position + 1);
                continue;
            }
            else
            {
                answer = false;
                return answer;
            }
        }
        return answer;
    }
};