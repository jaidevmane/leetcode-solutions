func longestPalindrome(s string) string {
    res := ""
    resLen := 0

    for i:= 0; i < len(s); i++{
        // odd case
        l, r := i, i
        for l >= 0 && r < len(s) && s[l] == s[r] {
            if (r -l + 1) > resLen{
                resLen = r - l + 1
                res = s[l: r + 1]
            }
            l--
            r++
        }

        // even case
        l, r = i, i + 1 
        for l >= 0 && r < len(s) && s[l] == s[r] {
            if (r - l + 1) > resLen{
                resLen = r - l + 1
                res = s[l: r + 1]
            }
            l--
            r++
        }

    }
    return res
    
}