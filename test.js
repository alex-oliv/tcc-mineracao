function formatDate(date) {
  let d = new Date(date),
    month = '' + (d.getMonth() + 1),
    day = '' + d.getDate(),
    year = d.getFullYear();

  if (month.length < 2) month = '0' + month;
  if (day.length < 2) day = '0' + day;

  return [year, month, day].join('');
}

//let today = Date()
let today = "Fri Jan 17 08:22:35 2020 -0300"

console.log(formatDate(today))


//commitDate = "Fri Jan 17 08:22:35 2020 -0300"
//result = "Thu Jun 16 2022 07:43:41 GMT-0300 (GMT-03:00)"