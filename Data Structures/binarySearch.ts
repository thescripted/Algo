function binarySearchList(arr: number[], v: number): number{
    let left = 0;
    let right = arr.length - 1;
    
    while (left < right) {
        const idx = left + Math.floor((right - left)/2);
        const value = arr[idx]
        if (value === v) {
            return idx
        }
        else if (value > v) {
            right = idx - 1;
        } else {
            left = idx + 1;
        }
    }
    return -1;
}

const list = [1, 5, 7, 9, 11, 15, 18];

console.log(binarySearchList(list, 17));
