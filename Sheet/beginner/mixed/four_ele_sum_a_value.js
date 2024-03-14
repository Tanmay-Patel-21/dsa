// Problem statement
// You are given an array/list 'ARR' of ‘N’ integers and an integer value ‘TARGET’. You need to check whether there exist four numbers (ARR[i], ARR[j], ARR[k], ARR[l]) such that (0 <= i < j < k < l < N) and ARR[i] + ARR[j] + ARR[k] + ARR[l] = 'TARGET'.

// Note:
// 1. All four numbers should exist at different indices in the given array.
// 2. The answer is case-sensitive.
// Detailed explanation ( Input/output format, Notes, Images )
// Constraints:
// 1 <= T <= 10^2
// 4 <= N <= 2*10^2   
// -10^9 <= ARR[i] <= 10^9
// -10^9 <= TARGET<= 10^9 

// Time Limit: 1 sec
// Follow Up:

// Can you try solving the problem with less than O(N^2 * log(N)) time complexity?
// Sample Input 1:
// 2
// 5 9
// 1 3 3 10 2
// 6 20
// 2 4 6 3 1 1
// Sample Output 1:
// Yes
// No
// Explanation For Sample Input 1:
// Test case 1:
// The elements at indices (0, 1, 2, 4) gives sum 9 i.e, ARR[0] + ARR[1] + ARR[2] + ARR[4] = 9. Hence the answer is Yes.

// Test case 2:
// None of the combinations of 4 numbers gives 20 as 'TARGET'. Hence the answer is No.  
// Sample Input 2:
// 2
// 5 15
// 0 10 1 2 2
// 6 20
// -2 12 -1 1 20 1 
// Sample Output 2:
// Yes
// Yes


/* Declare and implement your function here 
eg: function example(parameter_name1,parameter_name2....){}
Handle the input/output from main()
*/
function isFoursome(n, t, arr) {
    if (n < 4) return 'No';
    let sums = new Map();
    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            sums.set(arr[i] + arr[j], [i, j]);
        }
    }
    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            let sum = arr[i] + arr[j];
            if (sums.has(t - sum)) {
                let [t1, t2] = sums.get(t - sum);
                if ((i != t1 && j != t2) && (i != t2 && j != t1))
                    return 'Yes'
            }
        }
    }
    return 'No'
}