#include <iostream>
using namespace std;

int main()
{
    int n, x;
    int num[10001];
    int cnt = 0;
    cin >> n >> x;

    for(int i=0; i<n; i++)
    {
        int tmp;
        cin >> tmp;

        if(tmp < x)
        {
           num[cnt] = tmp;
           ++cnt;
        }
    }

    for(int j=0; j<cnt-1; j++)
        cout << num[j] << " ";
    cout << num[cnt-1] << endl;
}
