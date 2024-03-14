// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

// Example 1:
// Input: matrix = 1 2 3 
//                 4 5 6
//                 7 8 9
// Output: matrix= 7 4 1
//                 8 5 2
//                 9 6 3

 


var rotate = function (matrix) {
    let len = matrix.length;
    for (let i = 0; i < len; i++) {
        for (let j = i + 1; j < len; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }
    for (let i = 0; i < len; i++) {
        matrix[i].reverse();
    }
};