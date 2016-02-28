class Solution {
public:
    int evalRPN(vector<string> &tokens) {

        int result = 0;
        int i;
        stack<int> opd;         //存储操作数
        int size = tokens.size();
        for(i=0;i<size;i++)
        {
            if(tokens[i]=="*")
            {
                int rOpd = opd.top();   //右操作数
                opd.pop();
                int lOpd = opd.top();  //左操作数
                opd.pop();
                result = lOpd*rOpd;
                opd.push(result);
            }
            else if(tokens[i]=="/")
            {
                int rOpd = opd.top();
                opd.pop();
                int lOpd = opd.top();
                opd.pop();
                result = lOpd/rOpd;
                opd.push(result);
            }
            else if(tokens[i]=="+")
            {
                int rOpd = opd.top();
                opd.pop();
                int lOpd = opd.top();
                opd.pop();
                result = lOpd+rOpd;
                opd.push(result);
            }
            else if(tokens[i]=="-")
            {
                int rOpd = opd.top();
                opd.pop();
                int lOpd = opd.top();
                opd.pop();
                result = lOpd-rOpd;
                opd.push(result);
            }
            else
            {
                opd.push(atoi(tokens[i].c_str()));
            }
        }
        return opd.top();
    }
};
