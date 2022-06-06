const str = 'GuilhermeAvelino<gavelino@gmail.com>';

const onlyUpper1 = str.replace(/[a-z]/, '');
//console.log(onlyUpper1); // 👉️ "HW"

const onlyUpper2 = str.replace(/([A-Z])/g, ' $1').trim().split("<");
//console.log(onlyUpper2[0]); // 👉️ "HW"

const onlyUpper3 = str.match(/([A-Z])/g, ' $1');
//console.log(onlyUpper3); // 👉️ ['H', 'W']


// HERE 
const author = str.replace(/([A-Z])/g, ' $1').trim().split("<")[0];
console.log(author)