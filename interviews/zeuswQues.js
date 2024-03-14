// Write a program to reverse the alternate words in the string:
// Example:
// Input - 'My name is prince'
// Output - 'My eman is ecnirp'
console.log('asd');
function getStringArr(myStr) {
    let i = 0;
    let words = [];
    let currWord = "";
    while (i <= myStr.length) {
        if (myStr[i] === " " || i === myStr.length) {
            words.push(currWord);
            currWord = "";
        }
        else {
            currWord += myStr[i];
        }
        i++;
    }
    return words;
}

function reverseString(myStr) {
    let i = myStr.length - 1;
    let newStr = "";
    while (i >= 0) {
        newStr += myStr[i];
        i--;
    }
    return newStr;
}

function getAltRevString(myStr) {
    let newStr = getStringArr(myStr);
    let i = 0;
    let finalStr = '';
    while (i < newStr.length) {
        if (i % 2 === 0) {
            finalStr += newStr[i];
        }
        else {
            finalStr += reverseString(newStr[i]);
        }
        finalStr += " ";
        i++;
    }
    return finalStr;
}

console.log(getAltRevString("My name is prince"));

// console.log('asd')



// function getAltRevStr(myStr) {
//     let newStr = "";
//     let currWord = "";
//     let reverse = false;
//     let i = 0;
//     while (i <= myStr.length) {
//         let currChar = myStr[i];
//         if (currChar === " " || i === myStr.length) {
//             if (reverse) {
//                 newStr += reverseString(currWord);
//             } else {
//                 newStr += currWord;
//             }
//             newStr += " ";
//             currWord = "";
//             reverse = !reverse;
//         } else {
//             currWord += currChar;
//         }
//         i++;
//     }
//     console.log(newStr);
// }

// function reverseString(myStr) {
//     let newStr = "";
//     let i = myStr.length - 1;
//     while (i >= 0) {
//         newStr += myStr[i];
//         i--;
//     }
//     return newStr;
// }