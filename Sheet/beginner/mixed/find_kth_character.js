// You have been given an Encrypted String where repetitions of substrings are represented as substring followed by the count of substrings.

// Example: String "aabbbcdcdcd" will be encrypted as "a2b3cd3".
// You need to find the 'K'th character of Decrypted String. Decrypted String would have 1-based indexing.

// Note :

// Input string will always be lowercase characters without any spaces.

// If the count of a substring is 1 then also it will be followed by Integer '1'.
// Example: "aabcdee" will be Encrypted as "a2bcd1e2"
// This means it's guaranteed that each substring is followed by some Integer.

// Also, the frequency of encrypted substring can be of more than one digit. For example, in "ab12c3", ab is repeated 12 times. No leading 0 is present in the frequency of substring.

// The frequency of a repeated substring can also be in parts.
// Example: "aaaabbbb" can also have "a2a2b3b1" as Encrypted String.
// Detailed explanation ( Input/output format, Notes, Images )
// Sample Input 1 :
// a2b3cd3
// 8
// Sample Output 1 :
// c
//  Explanation to Sample Input 1 :
// S = "a2b3cd3"
// Decrypted String of S = "aabbbcdcdcd"
// According to 1-based indexing for S, the 8th character is 'c'.
// Sample Input 2 :
// ab12c3
// 20
// Sample Output 2 :
// b
//  Explanation to Sample Input 2 :
// S = "ab12c3"
// Decrypted String of S = "ababababababababababababccc"
// So 20th character is 'b'.


/* Declare and implement your function here 
eg: function example(parameter_name1,parameter_name2....){}
Handle the input/output from main()
*/
function getDecStr(str, pos) {
    let currentKey = str[0];
    let currentCount = 0;
    let intEnc = false;

    for (let i = 1; i < str.length; i++) {
        if (intEnc) {
            if (checkInt(str[i])) {
                currentCount = currentCount * 10 + parseInt(str[i]);

                // Check if the count exceeds the upper limit (10^18)
                if (currentCount > 1e18) {
                    return -1;  // Return an error value if count exceeds the limit
                }

                if (i == str.length - 1) {
                    currentCount = currentKey.length * currentCount;
                    return currentKey[(pos - 1) % currentKey.length];
                }
            }
            else {
                currentCount = currentKey.length * currentCount;

                // Check if the count exceeds the upper limit (10^18)
                if (currentCount > 1e18) {
                    return -1;  // Return an error value if count exceeds the limit
                }

                if (currentCount >= pos) {
                    return currentKey[(pos - 1) % currentKey.length];
                }
                else {
                    pos = pos - currentCount;
                    currentKey = str[i];
                    currentCount = 0;
                    intEnc = false;
                }
            }
        }
        else {
            if (!checkInt(str[i])) {
                currentKey += str[i];
            } else {
                if (i == str.length - 1) {
                    return currentKey[(pos - 1) % currentKey.length];
                }
                intEnc = true;
                currentCount = parseInt(str[i]);
            }
        }
    }
    return -1;
}


function checkInt(chr) {
    if (isNaN(parseInt(chr))) {
        return false;
    }
    return true;
}
