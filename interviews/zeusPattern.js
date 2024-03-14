function printPattern(n) {
    for (let i = 0; i < n; i++) {
        var rightNum = getRightNum(i, n - 1);
        console.log(rightNum.split('').reverse().join('') + '1' + rightNum);
    }
}
function getRightNum(noZ, k) {
    let rightNum = '';
    for (let i = 0; i < k; i++) {
        if (i >= noZ) {
            rightNum += '0';
        }
        else {
            rightNum += '1';
        }
    }
    return rightNum;
}

printPattern(10);