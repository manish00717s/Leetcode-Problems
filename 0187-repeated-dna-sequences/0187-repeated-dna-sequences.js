/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    let seen = new Set(), repeated = new Set();

    for (let i = 0; i <= s.length - 10; i++) {
        let sub = s.substring(i, i + 10);
        if (seen.has(sub)) repeated.add(sub);
        else seen.add(sub);
    }

    return [...repeated];
};