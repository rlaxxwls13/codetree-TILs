const fs = require("fs");
let arr = fs.readFileSync(0).toString().split("\n");
let a = Number(arr[0].split(" ")[0]);
let b = Number(arr[0].split(" ")[1]);
let c = Number(arr[1]);
console.log(a,b,c);