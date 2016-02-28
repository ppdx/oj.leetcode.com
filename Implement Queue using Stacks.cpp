class Queue {
    stack<int> _stack;
public:
    // Push element x to the back of queue.
    void push(int x) {
        stack<int> tmp;
        while (!_stack.empty())
        {
            tmp.push(_stack.top());
            _stack.pop();
        }
        tmp.push(x);
        while (!tmp.empty())
        {
            _stack.push(tmp.top());
            tmp.pop();
        }
    }

    // Removes the element from in front of queue.
    void pop(void) {
        _stack.pop();
    }

    // Get the front element.
    int peek(void) {
        return _stack.top();
    }

    // Return whether the queue is empty.
    bool empty(void) {
        return _stack.empty();
    }
};
