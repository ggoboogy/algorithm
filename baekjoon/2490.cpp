#include <iostream>
using namespace std;

int main()
{
    char result[3];
    for(int i=0; i<3; i++)
    {
        int cnt = 0;
        for(int j=0; j<4; j++)
        {   
            int num;
            cin >> num;
            if(num == 0) ++cnt;
        }

        if(cnt == 1)
            result[i] = 'A';
        else if(cnt == 2)
            result[i] = 'B';
        else if(cnt == 3)
            result[i] = 'C';
        else if(cnt == 4)
            result[i] = 'D';
        else
            result[i] = 'E';
    }
    cout << result[0] << endl << result[1] << endl << result[2] << endl;
}
