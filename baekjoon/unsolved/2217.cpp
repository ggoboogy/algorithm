#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

int lope[100000];
int main()
{
    int n;
    cin >> n;

    for(int i=0; i<n; i++)
        cin >> lope[i];

    sort(lope, lope+n, greater<int>());

    int current = lope[0];
    int cnt = 1;
    for(int i=1; i<n; i++)
    {
        if((lope[i]*(cnt+1)) >= (current*cnt))
        {
            current = lope[i];
            cnt += 1;
        }
    }
    cout << current*cnt << endl;
}
