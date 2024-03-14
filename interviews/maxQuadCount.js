function getMaxQuad(n, arr) {
    let quad = new Map();
    let diff = 1;
    while (diff < n) {
        let i = 0;
        let j = i + diff;
        while (j < n) {
            p = arr[i] * arr[j];
            if (quad.has(p)) {
                quad.set(p, quad.get(p) + 1);
            }
            else {
                quad.set(p, 1);
            }
            i++;
            j++;
        }
        diff++;
    }
    let q = 0;
    let count = 1;

    quad.forEach((val, key) => {
        if (val > count) {
            if (val == count) {
                q = Math.min(q, key);
            }
            else {
                count = val;
                q = key;
            }
        }
    });
    if (count == 1) return 0;
    return [q, getConsecSum(count)]
}
function getConsecSum(m) {
    sum = 0;
    for (i = 1; i < m; i++) {
        sum += i;
    }
    return sum;
}

// let arr = [2, 6, 3, 4, 1, 12];
// let arr = [4, 1, 7, 2, 6, 5];
let arr = [1, 2, 3, 4, 6, 8, 12, 24];
console.log(...getMaxQuad(arr.length, arr));