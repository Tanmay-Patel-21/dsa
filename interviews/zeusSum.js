function maxLenSum(arr, s) {
    let maxLen = 0
    for (let i = 0; i < arr.length; i++) {
        temp = 0;
        sum = 0;
        for (let j = i; j < arr.length; j++) {
            sum += arr[j];
            temp++;
            if (sum > s) {
                continue;
            }
            if (sum == s && temp > maxLen) {
                maxLen = temp;
            }
        }
    }
    return maxLen;
}

console.log(maxLenSum([1, -2, -1, 1, 1, 1, 2, 3, 4, 2, 6], 6))