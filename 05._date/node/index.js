console.log(new Date());

console.log(Date())

// get date as a unix timestamp
console.log(new Date().getTime());


/* Region specific */
console.log("======= Region specific ======");
const date = new Date();
console.log(new Intl.DateTimeFormat('en-US').format(date));
console.log(new Intl.DateTimeFormat('da-DK').format(date));