#include <iostream>
using namespace std;

int main()
{
    int n, m;
    int total = 0;
    int min = 10000;

    cin >> m;
    cin >> n;

    for(int i=m; i<=n; i++)
    {
        int k;
        for(k=2; k<i; k++)
            if(i%k == 0)
                break;

        if(k==i)
        {
            total += i;
            
            if(min > i)
                min = i;
        }
    }
    if(total == 0)
        cout << -1 << endl;
    else
        cout << total << endl << min << endl;
    
    return 0;
}
