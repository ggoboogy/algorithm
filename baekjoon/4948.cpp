#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n;
    int result[200000];
    int total = 0;

    while(1)
    {
        cin >> n;
        if(n == 0) break;
        
        int num = 0;
        for(int i=n+1; i<=2*n; i++)
        {
            if(i == 2 || i == 3)
            {
                ++num;
                continue;
            }
            if(i%2 == 0 || i == 1)
                continue;
            
            int limit = int(sqrt(i));
            int k;
            for(k=3; k<=limit; k++)
                if(i%k == 0) break;
            
            if(k == limit+1)
                ++num;
        }
        result[total] = num;
        ++total;
    }
    for(int k=0; k<total; k++)
        cout << result[k] << endl;
}
