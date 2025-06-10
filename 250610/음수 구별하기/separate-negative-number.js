const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

console.log(n);
if (n < 0) {
    console.log("minus");
}