#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str;
    cin >> str;

    for(int i=0; i<str.length(); i++)
    {
        cout << str[i];
        if(i%10 == 9)
            cout << endl;
    }
    if(str.length()%10 != 0)
        cout << endl; 
    return 0;
}
