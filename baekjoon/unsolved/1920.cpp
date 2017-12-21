#include <algorithm>
#include <cstdio>

int main()
{
    int n;
    scanf("%d", &n);

    int num[n];
    for(int i=0; i<n; i++)
        scanf("%d", &num[i]);

    std::sort(num, num+n);

    int m;
    int result[m];
    scanf("%d", &m);

    for(int i=0; i<m; i++)
    {
        int number;
        scanf("%d", &number);
        
        int left = 0;
        int right = n-1;
        int pivot = (n+1)/2;

        while(left < right)
        {
            if(num[pivot] == number)
            {
                result[i] = 1;
                break;
            }
            else if(num[pivot] < number)
            {
                left = pivot;
                pivot = left + (right-left+1)/2;
            }
            else
            {
                right = pivot;
                pivot = right - (right-left+1)/2;
            }
        }
        if(left >= right)
            result[i] = 0;
    }
    for(int i=0; i<m; i++)
        printf("%d\n", result[i]);
}
