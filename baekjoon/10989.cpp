#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    long long int n;
    int num[10001] = {0};
    cin >> n;
    
    for(int i=0; i<n; i++)
    {
        int number;
        scanf("%d", &number);
        num[number] += 1;
    }

    for(int i=0; i<10001; i++)
    {
        if(num[i])
        {
            for(int j=0; j<num[i]; j++)
                printf("%d\n",i);
        }
    }
}
