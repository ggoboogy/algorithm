#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    
    for(int i=min(a,b); i>0; i--)
    {
        if(a%i == 0 && b%i == 0)
        {
            cout << i << endl;
            break;
        }
    }
    for(int i=max(a,b); i<=a*b; i+=max(a,b))
    {
        if(i%min(a,b) == 0)
        {
            cout << i << endl;
            break;
        }
    }
}
