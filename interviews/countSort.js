function countSort(n, arr) {
    let maxi = 0;
    let mini = 0;

    for (let i = 0; i < n; i++) {
        if (arr[i] > maxi) {
            maxi = arr[i];
        }
        else if (arr[i] < mini) {
            mini = arr[i];
        }
    }
    count = [];
    for (let i = 0; i < maxi - mini + 1; i++) {
        count.push(0);
    }
    for (let i = 0; i < n; i++) {
        count[arr[i] - mini]++;
    }
    for (let i = 1; i < count.length; i++) {
        count[i] += count[i - 1];
    }

    output = [];
    for (let i = 0; i < n; i++) {
        output.push(0);
    }
    for (let i = n - 1; i >= 0; i--) {
        output[count[arr[i] - mini] - 1] = arr[i];
        count[arr[i] - mini]--;
    }

    return output;
}

arr = [-100, 142, 4, 47, 87, 9, 0, -69]
console.log(countSort(arr.length, arr));