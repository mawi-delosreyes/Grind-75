var isAnagram = function(s, t) {
  
    let s_mapping = new Map();

    if (s.length !== t.length) return false;

    for (let i=0; i<s.length; i++) {
        if (!s_mapping.has(s[i])) s_mapping.set(s[i], 1);
        else s_mapping.set(s[i], s_mapping.get(s[i])+1);
    }

    console.log(s_mapping);

    for (let i=0; i<t.length; i++) {
        if (!s_mapping.has(t[i]) || s_mapping.get(t[i]) === 0 || isNaN(s_mapping.get(t[i]))) return false;
        s_mapping.set(t[i], s_mapping.get(t[i])-1);
    }
    return true;    
};

console.log(isAnagram("abb", "aab"));