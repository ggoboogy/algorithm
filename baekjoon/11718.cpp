#include <iostream>
#include <string>
using namespace std;

int main()
{
    string input;
    string result[100];
    int i;

    for(i=0; i<100; ++i)
    {
        getline(cin, input);
        if(input == "") break;
        result[i] = input;
    }
    for(int k=0; k<i; k++)
        cout << result[k] << endl;

    return 0;
}
