#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    int total = 0;
    string number;
    cin >> n;
    cin >> number;

    for(int i=0; i<n; i++)
        total += (number[i] - '0');
    cout << total << endl;
    return 0;
}
