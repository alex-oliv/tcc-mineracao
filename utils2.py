import datetime

"""
function formatDate(date) {
  let d = new Date(date),
    month = '' + (d.getMonth() + 1),
    day = '' + d.getDate(),
    year = d.getFullYear();

  if (month.length < 2) month = '0' + month;
  if (day.length < 2) day = '0' + day;

  return [year, month, day].join('-');
}
"""


def formatDate(date):
    clear_date = datetime.datetime.strptime(date, '%c %z')

    return str(clear_date).split(' ')[0].replace('-', '')


x = datetime.datetime.now()
commitDate = "Fri Jan 17 08:22:35 2020 -0300"
#date_time_obj = datetime.datetime.strptime(x, '%d/%m/%y %H:%M:%S')
#date_time_obj =
#print(str(date_time_obj))

#print(str(date_time_obj).split(' ')[0].replace('-', ''))
print(formatDate(commitDate))
