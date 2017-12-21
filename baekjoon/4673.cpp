#include <iostream>
using namespace std;

int main()
{
    int number[10001] = {0};

    for(int i=1; i<10001; i++)
    {
        int num = i;
        int a,b,c,d,e;
        
        while(num < 10001)
        {
            a = num%10;
            b = num/10 %10;
            c = num/100 %10;
            d = num/1000 %10;
            e = num/10000 %10;

            num = num+a+b+c+d+e;
            if(num < 10001)
                number[num] = 1;
        }
    }

    for(int k=1; k<10001; k++)
    {
        if(number[k] != 1)
            cout << k << endl;
    }
}
