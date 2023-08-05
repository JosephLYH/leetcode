// Escalator Conversations
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int numCases;
    cin >> numCases;

    for (int i = 0; i < numCases; i++)
    {
        int count = 0;
        int numPeople, numSteps, stepSize, h;
        cin >> numPeople >> numSteps >> stepSize >> h;

        int maxDiff = stepSize * (numSteps - 1);
        for (int j = 0; j < numPeople; j++)
        {
            int height;
            cin >> height;

            int diff = abs(height - h);
            if (diff <= maxDiff && height != h && diff % stepSize == 0)
                count++;
        }

        cout << count << endl;
    }

    return 0;
}