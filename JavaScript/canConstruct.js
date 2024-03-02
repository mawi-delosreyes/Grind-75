var canConstruct = function(ransomNote, magazine) {
    
    for (let i=0; i<magazine.length; i++) {
        ransomNote = ransomNote.replace(magazine[i], "");
    }
    if(!ransomNote) return true
    return false

};

console.log(canConstruct("aab", "baa"))