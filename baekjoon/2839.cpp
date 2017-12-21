#include <iostream>
using namespace std;

int main()
{
    int a;
    cin >> a;

    int five=a/5;
    int three=0;
    int min_num = 1000;

    while(five >= 0)
    {
        int left = a - (five*5);
        three = left/3;
        
        if((five*5+three*3 == a) &&(min_num > (three+five)))
            min_num = three + five;
        
        five--;
    }
    
    if(min_num == 1000)
        cout << -1 << endl;
    else
        cout << min_num << endl;
    return 0;
}
