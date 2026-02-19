/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let i = a.length - 1, j = b.length - 1, carry = 0, res = "";

    while (i >= 0 || j >= 0 || carry) {
        let sum = carry;
        if (i >= 0) sum += +a[i--];
        if (j >= 0) sum += +b[j--];

        res = (sum % 2) + res;
        carry = Math.floor(sum / 2);
    }

    return res;
};
