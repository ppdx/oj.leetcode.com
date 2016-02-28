/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    function dfs(s) {
        var mi = calc(s);
        if (mi === 0) return [s];
        var res = [];
        for (var i = 0; i < s.length; i++) {
            if (s[i] === '(' || s[i] === ')') {
                var ss = s.slice(0, i) + s.slice(i + 1);
                if (!visited.has(ss) && calc(ss) < mi) {
                    visited.add(ss);
                    dfs(ss).forEach(function(item) {
                        res.push(item);
                    });
                }
            }
        }
        return res;
    }

    function calc(s) {
        var a, b, c;
        a = b = 0;
        for (c of s) {
            a += c === '(' ? 1 : (c === ')' ? -1 : 0);
            b += a < 0;
            a = Math.max(a, 0);
        }
        return a + b;
    }

    var visited = new Set([s]);
    return dfs(s);
};

(function() {
    for (let arg of arguments) {
        console.log(arg, ' -> ', removeInvalidParentheses(arg));
    }
})("()())()", "(a)())()", ")(");
