#include <iostream>
using namespace std;

int main()
{
    int n, k;
    cin >> n;
    cin >> k;
    
    int boonja = 1;
    int boonmo = 1;

    for(int i=1; i<=n; i++)
        boonja *= i;

    for(int i=1; i<=k; i++)
        boonmo *= i;

    for(int i=1; i<=n-k; i++)
        boonmo *= i;

    cout << boonja/boonmo << endl;
}
