// Winner

#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main()
{
    int n, maximum = 0;
    unordered_map<string, int> mp, mp2;
    string names[1000];
    int scores[1000];

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> names[i] >> scores[i];
        mp[names[i]] += scores[i];
    }

    for (auto [name, score] : mp)
        maximum = max(maximum, score);

    for (int i = 0; i < n; i++)
    {
        mp2[names[i]] += scores[i];
        if (mp2[names[i]] >= maximum && mp[names[i]] == maximum)
        {
            cout << names[i] << endl;
            return 0;
        }
    }

    return 0;
}