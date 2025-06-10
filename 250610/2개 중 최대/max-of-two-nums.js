const fs = require("fs");
let arr = fs.readFileSync(0).toString().trim().split(" ");
a = Number(arr[0]);
b = Number(arr[1]);
let result = a >= b ? a : b;
console.log(result);