const arr = ["a", "b", "c", "d"];

function basicIterator(arr) {
  let index = 0;

  return {
    next() {
      if ( index < arr.length){
        return {
          value : arr[index++],
          done  : false
        }
      } else {
        return {
          value: undefined,
          done: true,
        }
      }
    }
  }
}

const test = basicIterator(arr);
console.dir(test);
console.log(test.next());
console.log(test.next());
console.log(test.next());
console.log(test.next());