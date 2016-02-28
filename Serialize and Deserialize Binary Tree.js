// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = val;
    this.left = left || null;
    this.right = right || null;
}


/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    var data = [],
        stack = [root];
    while (stack.length) {
        var current = stack.pop();
        if (current) {
            data.push(current.val);
            stack.push(current.right);
            stack.push(current.left);
        } else {
            data.push(null)
        }
    }
    return JSON.stringify(data);
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    return resume(JSON.parse(data));
};

function resume(data) {
    var val = data.shift();
    if (val!==null) {
        var node = new TreeNode(val);
        node.left = resume(data);
        node.right = resume(data);
        return node;
    } else {
        return null;
    }
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */

(function() {
    var root = new TreeNode(1, new TreeNode(2), new TreeNode(3, null, new TreeNode(4)));
    console.log(root);
    var ser = serialize(root);
    console.log(ser);
    var deser = deserialize(ser);
    console.log(deser);
})();
