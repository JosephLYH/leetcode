// Escalator Conversations
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int numCases;
    cin >> numCases;

    for (int i = 0; i < numCases; i++)
    {
        vector<int> orignal, sorted;

        int n;
        cin >> n;

        for (int j = 0; j < n; j++)
        {
            int num;
            cin >> num;

            orignal.push_back(num);
            sorted.push_back(num);
        }

        sort(sorted.begin(), sorted.end());

        int flag = 0;
        for (int j = 0; j < n; j++)
        {
            if (orignal[j] % 2 != sorted[j] % 2)
            {
                cout << "NO" << endl;
                flag = 1;
                break;
            }
        }

        if (flag == 0)
            cout << "YES" << endl;
    }

    return 0;
}