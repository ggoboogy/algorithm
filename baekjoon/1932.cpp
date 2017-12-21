#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int data[n][n];
    int dp[n][n];

    for(int i=0; i<n; i++)
        for(int j=0; j<=i; j++)
            cin >> data[i][j];

    for(int k=n-1; k>=0; k--)
    {
        for(int j=0; j<=k; j++)
        {
            if(k==n-1)
                dp[k][j] = data[k][j];
            else
            {
                dp[k][j] = data[k][j] + max(dp[k+1][j],dp[k+1][j+1]);
            }
        }
    }
    cout << dp[0][0] <<endl;
    return 0;
}
