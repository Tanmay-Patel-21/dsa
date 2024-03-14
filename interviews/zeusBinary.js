function reverseBinary(n) {
    if (n > 255 || n < 0) {
        console('Number should be between 0-255')
    }
    else {
        let temp = [];
        let a = 0;
        for (let i = 0; i < 8; i++) {
            temp.push(n % 2);
            n = Math.floor(n / 2);
        }
        console.log(temp.join(''));
        for (let i = 0; i < 8; i++) {
            if (temp[i] == 1) {
                a += 2 ** (7 - i);
            }
        }
        return a;
    }
}

console.log(reverseBinary(18));