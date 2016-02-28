#include <queue>
#include <iostream>
using namespace std;

class Stack
{
    queue<int> my_stack;
public:
    // Push element x onto stack.
    void push(int x)
    {
        int len=my_stack.size();
        my_stack.push(x);
        for(int i=0; i<len; i++)
        {
            my_stack.push(my_stack.front());
            my_stack.pop();
        }
    }

    // Removes the element on top of the stack.
    void pop(void)
    {
        my_stack.pop();
    }

    // Get the top element.
    int top(void)
    {
        return my_stack.front();
    }

    // Return whether the stack is empty.
    bool empty(void)
    {
        return my_stack.size()==0;
    }
};

int main(){
    Stack st;
    for(int i=0;i<10;i++)
    {
        st.push(i);
    }
    while(!st.empty())
    {
        cout<<st.top()<<endl;
        st.pop();
    }
}
