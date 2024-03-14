function rotateMatRight(mat, n, m, k) {
    k = k % m;
    if (k === 0) return mat;
    mat.forEach((row) => {
        // target last k elements
        i = m - k;
        j = m - 1;
        while (i < j) {
            temp = row[i];
            row[i] = row[j];
            row[j] = temp;
            i++;
            j--
        }

        // target first m-k elements
        i = 0;
        j = m - k - 1;
        while (i < j) {
            temp = row[i];
            row[i] = row[j];
            row[j] = temp;
            i++;
            j--
        }
        //target entire array
        i = 0;
        j = m - 1;
        while (i < j) {
            temp = row[i];
            row[i] = row[j];
            row[j] = temp;
            i++;
            j--
        }
    });
    return matToArr(mat);
}
function matToArr(mat) {
    let ans = [];
    mat.forEach((row) => {
        row.forEach((ele) => {
            ans.push(ele);
        })
    })
    return ans;
}

mat = [[1107, 8773, 23990, 7124, 11114, 3587, 9369, 3680, 20065]]

rotations = 100;

console.log(...rotateMatRight(mat, mat.length, mat[0].length, rotations));