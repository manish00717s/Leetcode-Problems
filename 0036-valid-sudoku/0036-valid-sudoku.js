/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    let rows = Array(9).fill(0).map(() => new Set());
    let cols = Array(9).fill(0).map(() => new Set());
    let boxes = Array(9).fill(0).map(() => new Set());

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            let val = board[r][c];
            if (val === '.') continue;

            let box = Math.floor(r/3)*3 + Math.floor(c/3);

            if (rows[r].has(val) || cols[c].has(val) || boxes[box].has(val))
                return false;

            rows[r].add(val);
            cols[c].add(val);
            boxes[box].add(val);
        }
    }

    return true;
};
