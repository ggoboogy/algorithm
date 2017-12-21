#include <iostream>
using namespace std;

int main()
{
    int n;
    int num[100];
    int total = 0;
    cin >> n;

    for(int i=0; i<n; i++)
    {
        cin >> num[i];
        int j;
        for(j=2; j<num[i]; j++)
        {
            if((num[i]%j) == 0)
                break;
        }
        if(j==num[i])
            total += 1;
    }
    cout << total << endl;
    return 0;
}
