#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

template<class T>
ostream& operator << (ostream& o, vector<T> v)
{
    o << "[ ";
    for (int i = 0; i < v.size(); i++)
    {
        o << v[i] << " ";
    }
    o << "]";
    return o;
}

class Solution
{
    struct Position
    {
        int row, col;
        Position(int _row = 0, int _col = 0) :row(_row), col(_col) {}
    };
public:
    Solution() :colums(9, vector<bool>(10, false)), rows(9, vector<bool>(10, false)),
        squares(9, vector<bool>(10, false)), space()
    {
    }

    void solveSudoku(vector<vector<char> > &board)
    {
        fullData(board);
        vector<int> stack;
        int size = space.size() - 1;
        int i = -1;
        while (i < size)
        {
            //cout << stack << endl;
            char next = findNext(i + 1);
            if (next == 0)
            {
                while (i >= 0)
                {
                    deleteData(i, stack[i]);
                    next = findNext(i, stack[i] + 1);
                    if (next != 0)
                        break;
                    i--;
                    stack.pop_back();
                }
                setData(i, next);
                stack[i] = next;
            }
            else
            {
                i++;
                stack.push_back(next);
                setData(i, next);
            }
        }

        Position p;
        for (int i = 0; i < stack.size(); i++)
        {
            p = space[i];
            board[p.row][p.col] = stack[i]+'0';
        }
    }
private:
    void fullData(vector<vector<char> > &board)
    {
        char c;
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                c = board[i][j];
                if (c != '.')
                {
                    c -= '0';
                    colums[j][c] = true;
                    rows[i][c] = true;
                    squares[j / 3 + 3 * (i / 3)][c] = true;
                }
                else
                {
                    space.push_back(Position(i, j));
                }
            }
        }
    }

    int findNext(int i, int now = 1)
    {
        if (now>9)
        {
            return 0;
        }
        auto p = space[i];
        while (colums[p.col][now] || rows[p.row][now]
            || squares[p.col / 3 + 3 * (p.row / 3)][now])
        {
            if (now >= 9)
            {
                return 0;
            }
            else
            {
                now++;
            }
        }
        return now;
    }

    void deleteData(int i, int d)
    {
        Position p = space[i];
        colums[p.col][d] = false;
        rows[p.row][d] = false;
        squares[p.col / 3 + 3 * (p.row / 3)][d] = false;
    }
    void setData(int i, int d)
    {
        Position p = space[i];
        colums[p.col][d] = true;
        rows[p.row][d] = true;
        squares[p.col / 3 + 3 * (p.row / 3)][d] = true;
    }

    vector<vector<bool>> colums;
    vector<vector<bool>> rows;
    vector<vector<bool>> squares;

    vector<Position> space;
};

void print_board(vector<vector<char>> &board)
{
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    vector<vector<char>> board{
        { '5', '3', '.', '.', '7', '.', '.', '.', '.' },
        { '6', '.', '.', '1', '9', '5', '.', '.', '.' },
        { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
        { '8', '.', '.', '.', '6', '.', '.', '.', '3' },
        { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
        { '7', '.', '.', '.', '2', '.', '.', '.', '6' },
        { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
        { '.', '.', '.', '4', '1', '9', '.', '.', '5' },
        { '.', '.', '.', '.', '8', '.', '.', '7', '9' } };

    print_board(board);
    Solution sol;
    sol.solveSudoku(board);
    print_board(board);

}