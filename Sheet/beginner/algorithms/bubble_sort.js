// Bubble Sort is one of the sorting algorithms that works by repeatedly swapping the adjacent elements of the array if they are not in sorted order.

// You are given an unsorted array consisting of N non-negative integers. Your task is to sort the array in non-decreasing order using the Bubble Sort algorithm.

// For Example:
// Bubble Sort implementation for the given array:  {6,2,8,4,10} is shown below :-
// Itr 1: 6-2 8 4 10
// Itr 2: 2 6 8-4 10
// Itr 3: 2 6-4 8 10
// Itr 4: 2 4 6 8 10
// Itr 5: 2 4 6 8 10

function bubbleSort(arr, l) {
    for (var i = 0; i < l - 1; i++) {
        for (var j = 1; j < l - i; j++) {
            if (arr[j - 1] > arr[j]) {
                let temp = arr[j - 1];
                arr[j - 1] = arr[j];
                arr[j] = temp;
            }
        }
    }
    return arr.join(" ")
}