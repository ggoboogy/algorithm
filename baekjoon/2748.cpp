#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    long array[91];
    cin >> n;

    for(int i=0; i<=n; i++)
    {
        if(i == 0 || i == 1)
            array[i] = i;
        else
            array[i] = array[i-1] + array[i-2];
    }
    cout << array[n] << endl;
}
