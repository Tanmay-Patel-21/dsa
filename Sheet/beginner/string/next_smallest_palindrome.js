// You are given a number 'N' in the form of a string 'S', your task is to find the smallest number strictly greater than the given number 'N' which is a palindrome.

// Note:

// 1) A palindrome is a word, number, phrase, or another sequence of characters that reads the same backward as forward, such as 'naman', 'abcba', '1234321', etc
// 2) The numerical value of the given string 'S' will be greater than 0.
// 3) A single-digit number is also considered as a palindrome.
// 4) Note that the length of the string 'S' is nothing but the number of digits in the number 'N'.

// Sample Input 1:
// 1
// 4
// 1221
// Sample Output 1:
// 1331
// Explanation for sample input 1:
// The next smaller palindrome to 1221 is 1331, as it is strictly greater than 1221 and it reads the same from the front and back both.
// Sample Input 2:
// 1
// 3
// 999
// Sample Output 2:
// 1001
// Explanation for sample input 1:
// The next smaller palindrome to 999 is 1001, as it is strictly greater than 999 and it reads the same from the front and back both.

function getPalindrome(p, n) {
    // Return the next one digit number for numbers 0-8
    if (p == 1 && n < 9) {
        return n + 1;
    }
    // For numbers containing only 9 as their digits
    else if ((n + 1) % (10 ** p) == 0) {
        return n + 2;
    }
    else {
        // For even length numbers
        if (p % 2 == 0) {
            let leftHalf = parseInt(n / 10 ** (p / 2));
            let rightHalf = (n % 10 ** (p / 2));
            let leftReverse = parseInt(leftHalf.toString().split('').reverse().join(''));
            if (leftReverse <= rightHalf) {
                leftHalf = leftHalf + 1;
                leftReverse = parseInt(leftHalf.toString().split('').reverse().join(''));
            }
            return leftHalf * (10 ** (p / 2)) + leftReverse;

        }
        // For odd length numbers
        else {
            // Divide number in to three parts, median, left half, and, right half
            // If the reverse of left Half is greater than the right half, then simply replace the right half with the reverse of left half
            // Else add
            let leftHalf = parseInt(n / 10 ** ((p + 1) / 2));
            let rightHalf = (n % 10 ** ((p - 1) / 2));
            let centerEle = parseInt(n / 10 ** ((p - 1) / 2)) % 10;
            let leftReverse = parseInt(leftHalf.toString().split('').reverse().join(''));

            if (leftReverse <= rightHalf) {
                leftHalf = (leftHalf * 10) + centerEle + 1;
                leftReverse = parseInt(leftHalf.toString().slice(0, -1).split('').reverse().join(''));
                return leftHalf * (10 ** ((p - 1) / 2)) + leftReverse;
            }
            return (leftHalf * (10 ** ((p + 1) / 2))) + (centerEle * (10 ** ((p - 1) / 2))) + leftReverse;
        }
    }
}