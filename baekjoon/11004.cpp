#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int num[5000000];
int main()
{
    int n, k;
    cin >> n >> k;

    for(int i=0; i<n; i++)
        scanf("%d", &num[i]);

    sort(num, num+n);
    printf("%d\n", num[k-1]);
}
