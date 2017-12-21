#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int data[n][2];
    for(int i=0; i<n; i++)
        cin >> data[i][0] >> data[i][1];
    
    int dp[n] = {0};
    for(int i=n-1; i>=0; i--)
    {
        if((i+data[i][0]-1) > n-1)
            dp[i] = 0;
        else
        {
            if(i+data[i][0]-1  == n-1)
                dp[i] = data[i][1];
            else
            {
                int next = i + data[i][0];
                int max_val = 0;
                for(int j=next; j<n; j++)
                    if(dp[j] > max_val)
                        max_val = dp[j];

                dp[i] = data[i][1] + max_val;
            }
        }
    }
    int result = 0;
    for(int k=0; k<n; k++)
        if(dp[k] > result)
            result = dp[k];
    cout << result << endl;
}

