#include <cstdio>
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n, m;
    scanf("%d %d", &m, &n);

    if(m == 1)
        m += 1;

    if(m == 2 && m <= n)
        printf("%d\n", 2);
    
    if(m%2 == 0)
        m += 1;

    for(int i=m; i<=n; i+=2)
    {
        int k;
        int end = int(sqrt(i));
        for(k=3; k<=end; k+=2)
        {
            if(i%k == 0)
                break;
        }
        if(k>end)
            printf("%d\n", i);
    }
    return 0;
}
