var isValid = s => {
    let st = [], m = {')':'(',']':'[','}':'{'};
    for (let c of s) {
        if (m[c]) {
            if (st.pop() !== m[c]) return false;
        } else st.push(c);
    }
    return !st.length;
};
