// You are given a square matrix, return true if the matrix is symmetric otherwise return false.

// A symmetric matrix is that matrix whose transpose is equal to the matrix itself.

// Example of symmetric matrix :
// 1 2 3   1 2 3
// 2 4 5 = 2 4 5
// 3 5 8   3 5 8
// (Transpose is changing rows into columns)

function strToArr(n, inStr) {
    let numbers = inStr.split(" ").map(Number);
    let inArr = [];

    for (let i = 0; i < numbers.length; i += n) {
        inArr.push(numbers.slice(i, i + n));
    }
    return inArr;
}

function isSymmetric(n, inArr) {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i == j) continue;
            if (inArr[i][j] != inArr[j][i]) return 'No';
        }
    }
    return 'Yes';
}


