function setMatrixZero(mat) {
    let row = [];
    let col = [];
    let newMat = [[], [], [], [], []];
    for (let i = 0; i < 5; i++) {
        if (row.includes(i)) {
            continue;
        } else {
            for (let j = 0; j < 5; j++) {
                if (mat[i][j] == 0) {
                    if (!row.includes(i)) {
                        row.push(i);
                    }
                    if (!col.includes(j)) {
                        col.push(j);
                    }
                }
            }
        }
    }
    console.log(row)
    console.log(col)
    for (let i = 0; i < 5; i++) {
        if (row.includes(i)) {
            newMat[i] = [0, 0, 0, 0, 0];
        }
        else {
            for (let j = 0; j < 5; j++) {
                if (col.includes(j)) {
                    newMat[i][j] = 0;
                }
                else {
                    newMat[i][j] = 1;
                }
            }
        }
    }
    return newMat;
}
let a = [
    [1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1]
]
console.log(setMatrixZero(a));
