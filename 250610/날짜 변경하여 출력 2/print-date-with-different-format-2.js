const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("-");
let mm = Number(input[0]);
let dd = Number(input[1]);
let yyyy = Number(input[2]);
console.log(`${yyyy}.${mm}.${dd}`);