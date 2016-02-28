/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    var len = secret.length,
        bull = 0,
        cows = 0,
        i;
    for (i = 0; i < len; i++) {
        bull += secret[i] === guess[i];
    }
    for (i = 0; i < 10; i++) {
        cows += Math.min(count(secret, i.toString()), count(guess, i.toString()));
    }

    return bull + 'A' + (cows - bull) + 'B';
};

function count(str, chr) {
    var i, c = 0;
    for (i = 0; i < str.length; i++) {
        c += str[i] === chr;
    }
    return c;
}

(function() {
    console.log(getHint('1000', '0111'));
})();
