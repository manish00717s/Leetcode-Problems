var permuteUnique = function(nums) {
    let res = [];
    nums.sort((a, b) => a - b);
    const backtrack = (path, used) => {
        if (path.length === nums.length) {
            res.push([...path]);
            return;
        }
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.push(nums[i]);
            backtrack(path, used);
            path.pop();
            used[i] = false;
        }
    };
    backtrack([], []);
    return res;
};
