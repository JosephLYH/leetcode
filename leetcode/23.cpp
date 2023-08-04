#include <queue>
#include <vector>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        // comparator for priority queue
        auto cmp = [](ListNode *a, ListNode *b)
        {
            return a->val > b->val;
        };

        // priority queue for O(logk) insertion
        priority_queue<ListNode *, vector<ListNode *>, decltype(cmp)> pq(cmp);
        // push all lists into priority queue in O(klogk)
        for (auto list : lists)
        {
            if (list)
                pq.push(list);
        }

        // merge lists in O(nlogk)
        // O(logk) for pop and O(logk) for push, O(n) for n nodes in total
        ListNode *head = new ListNode();
        for (ListNode *cur = head; !pq.empty(); cur = cur->next)
        {
            cur->next = pq.top();
            pq.pop();
            if (cur->next->next)
                pq.push(cur->next->next);
        }

        return head->next;
    }
};