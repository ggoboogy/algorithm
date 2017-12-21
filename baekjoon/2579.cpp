#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int stair[n+1] = {0};
    int dp[n+1];

    for(int i=1; i<=n; i++)
        cin >> stair[i];

    dp[0] = 0;
    dp[1] = stair[1];
    dp[2] = dp[1] + stair[2];
    
    for(int j=3; j<=n; j++)
        dp[j] = stair[j] + max(dp[j-2], stair[j-1]+dp[j-3]);
   
    cout << dp[n] << endl;
}
