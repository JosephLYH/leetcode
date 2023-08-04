#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool containsNearbyDuplicate(vector<int> &nums, int k)
    {
        unordered_map<int, int> last_seen;

        for (int i = 0; i < nums.size(); i++)
        {
            if (last_seen.count(nums[i]) && i - last_seen[nums[i]] <= k)
                return true;

            last_seen[nums[i]] = i;

            if (i >= k)
                last_seen.erase(nums[i - k]);
        }

        return false;
    }
};