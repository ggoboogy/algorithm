#include <iostream>
using namespace std;

int main()
{
    int t;
    int result[1001] = {0};
    cin >> t;

    for(int i=0; i<t; i++)
    {
        int a, b;
        cin >> a >> b;

        int j;
        for(j=max(a,b); j<=a*b; j+=max(a,b))
        {
            if(j%a == 0 && j%b == 0)
                break;
        }
        result[i] = j;
    }
    for(int i=0; i<t; i++)
        cout << result[i] << endl;

}
