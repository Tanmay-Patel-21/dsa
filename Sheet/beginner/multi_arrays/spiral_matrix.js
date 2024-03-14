// For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:

// a. First row(left to right)
// b. Last column(top to bottom)
// c. Last row(right to left)
// d. First column(bottom to top)
//  Mind that every element will be printed only once.

//  Sample Input 1:
// 1
// 4 4 
// 1 2 3 4 
// 5 6 7 8 
// 9 10 11 12 
// 13 14 15 16
// Sample Output 1:
// 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

function spiralOrder(actMatrix, row, col) {
    let sprOrd = [];
    let top = 0;
    let bottom = row;
    let left = 0;
    let right = col;
    let hd = 1;
    let vd = 0;
    let current = [0, 0]

    while (sprOrd.length < (row * col)) {
        if (hd === 1) {
            for (let i = current[1]; i < right; i++) {
                sprOrd.push(actMatrix[current[0]][i]);
                if (i === right - 1) {
                    hd = 0;
                    vd = 1;
                    current[1] = i;
                    current[0]++;
                    top++;
                }
            }
        }
        else if (hd === -1) {
            for (let i = current[1]; i >= left; i--) {
                sprOrd.push(actMatrix[current[0]][i]);
                if (i === left) {
                    hd = 0;
                    vd = -1;
                    current[1] = i;
                    current[0]--;
                    bottom--;
                }
            }
        }
        else if (vd === 1) {
            for (let i = current[0]; i < bottom; i++) {
                sprOrd.push(actMatrix[i][current[1]]);
                if (i === bottom - 1) {
                    hd = -1;
                    vd = 0;
                    current[0] = i;
                    current[1]--;
                    right--;
                }
            }
        }
        else if (vd === -1) {
            // sprOrd.push(0)
            for (let i = current[0]; i >= top; i--) {
                sprOrd.push(actMatrix[i][current[1]]);
                // sprOrd.push(0);
                if (i === top) {
                    hd = 1;
                    vd = 0;
                    current[0] = i;
                    current[1]++;
                    left++;
                }
            }
        }
    }
    return sprOrd.join(" ");
}
