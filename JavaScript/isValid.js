var isValid = function(s) {
    const holder = [];
    const mapping = {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }

    for (let i=0; i<s.length; i++) {
        let str = s[i];
        if (str === '}' || str === ']' || str ===')') {
            if (mapping[str] !== holder.pop()) {
                return false;
            }
        } else {
            holder.push(str);
        }
    }

    if (holder.length > 0) { return false; }
    return true;
};


console.log(isValid("()"));
