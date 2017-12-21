#include <iostream>
using namespace std;

int main()
{
    int n;
    int result = 1;
    cin >> n;

    for(int i=1; i<=n; i++)
        result *= i;

    cout << result << endl;
}
