#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int t;
    int prime[10001] = {0};
    cin >> t;

    int num[t];
    for(int i=0; i<t; i++)
        cin >> num[i];

    for(int i=2; i<=10000; i++)
    {
        if(i == 2 || i == 3)
        {
            prime[i] = 1;
            continue;
        }
        if(i%2 == 0 || i == 1)
            continue;
        
        int limit = int(sqrt(i));
        int k;
        for(k=3; k<=limit; k++)
            if(i%k == 0) break;
        
        if(k == limit+1)
            prime[i] = 1;
    }

    for(int j=0; j<t; j++)
    {
        int min = 10000;
        int left = 0;
        int right = 0;
        for(int k=2; k<=int(num[j]/2); k++)
        {
            if((prime[k] == 1) && (prime[num[j]-k] == 1))
            {
                if((num[j]-k-k) < min)
                {
                    left = k;
                    right = num[j] - k;
                    min = num[j] - k - k;
                }
            }
        }
        cout << left << " " << right << endl;
    }
}
