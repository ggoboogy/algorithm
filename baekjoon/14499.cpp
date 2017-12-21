#include <iostream>
using namespace std;

int main()
{
    int n, m, x, y, k;
    cin >> n >> m >> y >> x >> k;

    int map[n][m];
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> map[i][j];

    int result[k];
    int dice[6] = {0};
    int bottom = 5;
    int top = 0;
    int left = 3;
    int right = 2;
    int north = 1;
    int south = 4;
    int move_cnt = 0;    
    for(int i=0; i<k; i++)
    {
        int cmd, tmp;
        int move_flag = 0;
        
        cin >> cmd;
        switch(cmd)
        {
            case 1: // east
                if(x+1 < m)
                {
                    x += 1;
                    tmp = top;
                    top = left;
                    left = bottom;
                    bottom = right;
                    right = tmp;
                    move_flag = 1;
                }
                break;
            case 2: // west
                if(x-1 >= 0)
                {
                    x -= 1;
                    tmp = left;
                    left = top;
                    top = right;
                    right = bottom;
                    bottom = tmp;
                    move_flag = 1;
                }
                break;
            case 3: // north
                if(y-1 >= 0)
                {
                    y -= 1;
                    tmp = top;
                    top = south;
                    south = bottom;
                    bottom = north;
                    north = tmp;
                    move_flag = 1;
                }
                break;
            case 4: // south
                if(y+1 < n)
                {
                    y += 1;
                    tmp = top;
                    top = north;
                    north = bottom;
                    bottom = south;
                    south = tmp;
                    move_flag = 1;
                }
                break;
        }
        if(move_flag == 0)
            continue;
        
        if(map[y][x] == 0)
            map[y][x] = dice[bottom];
        else
        {
            dice[bottom] = map[y][x];
            map[y][x] = 0;
        }
        result[move_cnt] = dice[top];
        move_cnt += 1;
    }
    for(int i=0; i<move_cnt; i++)
        cout << result[i] << endl;
}
