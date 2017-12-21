#include <iostream>
using namespace std;

int main()
{
    int n, m;
    int y, x, d;

    cin >> n >> m;
    cin >> y >> x >> d;

    int data[n][m];
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> data[i][j];
    
    int cnt = 0;
    int flag = 0;
    while(1)
    {
        if(data[y][x] == 0)
        {
            data[y][x] = 2;
            cnt += 1;
        }
        if(d == 0)
        {
            d = 3;
            if((data[y][x-1] == 0) && (x-1 >= 0))
            {
                x -= 1;
                flag = 0;
            }
            else
                flag += 1;
        }
        else if(d == 1)
        {
            d = 0;
            if((data[y-1][x] == 0) && (y-1 >= 0))
            {
                y -= 1;
                flag = 0;
            }
            else
                flag += 1;
        }
        else if(d == 2)
        {
            d = 1;
            if((data[y][x+1] == 0) && (x+1 < m))
            {
                x += 1;
                flag = 0;
            }
            else
                flag += 1;
        }
        else if(d == 3)
        {
            d = 2;
            if((data[y+1][x] == 0) && (y+1 < n))
            {
                y += 1;
                flag = 0;
            }
            else
                flag += 1;
        }

        if(flag == 4)
        {
            if(d == 0 && y+1 < n && data[y+1][x] != 1)
                y += 1;
            
            else if(d == 1 && x-1 >= 0 && data[y][x-1] != 1)
                x -= 1;
                
            else if(d == 2 && y-1 >= 0 && data[y-1][x] != 1)
                y -= 1;

            else if(d == 3 && x+1 < m && data[y][x+1] != 1)
                x += 1;
 
            else
                break;

            flag = 0;
        }
    }
    cout << cnt << endl;
}
