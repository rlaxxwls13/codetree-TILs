const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

if (n < 0) {
    console.log("ice");
} else if (n >= 100) {
    console.log("vapor");
} else {
    console.log("water");
}