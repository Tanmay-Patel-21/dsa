function getSubarraysWithGivenSum(n, arr, t) {
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (arr[i] == t) {
            count++;
        }
    }
    for (let i = 0; i < n - 1; i++) {
        let sum = arr[i];
        for (let j = i + 1; j < n; j++) {
            sum += arr[j];
            if (sum == t) {
                count++;
            }
        }
    }
    return count;
}

// 2
// 4 6
// 3 1 2 4
// 3 3
// 1 2 3
let arr = [11, 49, 63, 15, 16, 5, 55, 78, 17, 83, 25, 72, 12, 84, 18, 44, 60, 27, 53, 90, 45, 88, 57]
console.log(getSubarraysWithGivenSum(arr.length, arr, 5));