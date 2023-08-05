// Theatre Square

#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n, m, a, x, y;

    cin >> n >> m >> a;
    x = n / a;
    y = m / a;

    if (n % a)
        x++;
    if (m % a)
        y++;

    cout << (long long)x * y << endl;

    return 0;
}