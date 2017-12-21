#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    int i;

    for(i=0; i<100; i++)
    {
        string tmp;
        getline(cin, tmp);
        cout << tmp << endl;
    }
    return 0;
}
