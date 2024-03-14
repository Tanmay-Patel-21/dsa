// Problem statement
// You have been given an integer array/list(ARR) of size 'N'. It only contains 0s, 1s and 2s. Write a solution to sort this array/list.

// Note :
// Try to solve the problem in 'Single Scan'. ' Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each element in the array/list just once.
// Detailed explanation ( Input/output format, Notes, Images )
// Constraints :
// 1 <= T <= 10
// 1 <= N <= (5 * (10 ^ 5))
// 0 <= ARR[i] <= 2

// Where 'N' is the size of the given array/list.
// And, ARR[i] denotes the i-th element in the array/list.

// Time Limit: 1sec 
// Sample Input 1 :
// 2
// 6
// 0 1 2 2 1 0
// 7
// 0 1 2 1 2 1 2
// Sample Output 1 :
// 0 0 1 1 2 2
// 0 1 1 1 2 2 2
// Sample Input 2 :
// 2
// 7
// 2 2 2 1 1 1 0
// 6
// 2 1 2 0 1 0
// Sample Output 2 :
// 0 1 1 1 2 2 2
// 0 0 1 1 2 2

function sort(arr) {
    let low = 0;
    let mid = 0;
    let high = arr.length - 1;
    let temp = 0;
    while (mid <= high) {
        if (arr[mid] == 0) {
            temp = arr[low];
            arr[low] = arr[mid];
            arr[mid] = temp;
            mid++;
            low++;
        }
        else if (arr[mid] == 1) { mid++; }
        else {
            temp = arr[high];
            arr[high] = arr[mid];
            arr[mid] = temp;
            high--;
        }
    }
}