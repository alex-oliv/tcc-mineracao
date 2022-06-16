import json


f = open('result.json')

data = json.load(f)
f.close()


def remove_duplicates(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)

    return result


def parse_dates_same_day(count, dates, issue_type):
    non_repeated_dates = remove_duplicates(dates)
    non_repeated_dates.sort()

    for i in non_repeated_dates:
        if str(i) in count:
            previous_info = count[str(i)]
            count[str(i)] = [previous_info[0], {
                "total": dates.count(i), "type": issue_type}]
        else:
            count[str(i)] = [{"total": dates.count(i), "type": issue_type}]
        
        


dates_created = []
dates_closed = []
count = {}

for issue in data['issues']:
    dates_created.append(issue['created_at'].split('T')[0].replace('-', ''))
    dates_closed.append(issue['closed_at'].split('T')[0].replace('-', ''))


parse_dates_same_day(count, dates_created, 'created')
parse_dates_same_day(count, dates_closed, 'closed')

dates = {}
dates['dates'] = count

"""dates = {
  "dates": [
    {
      "20201123": [
        {
          "total": 6,
          "type": "created"
        }
      ]
    },
    {
      "20201207": [
        {
          "total": 5,
          "type": "created"
        }
      ]
    },
    {
      "20201209": [
        {
          "total": 7,
          "type": "created"
        }
      ]
    },
    {
      "20201215": [
        { "total": 3, "type": "created" },
        { "total": 7, "type": "closed" }
      ]
    }
  ]
}
"""


lines = []
lines.append(json.dumps(dates))

with open('result2.json', 'w+') as writer:
    writer.writelines(lines)
    writer.close()
