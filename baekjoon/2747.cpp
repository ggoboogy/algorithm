#include <iostream>
using namespace std;

int main()
{
    int n;
    int array[50];
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
