import json


def remove_duplicates(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)

    return result


def parse_dates(count, dates, issue_type):
    non_repeated_dates = remove_duplicates(dates)
    non_repeated_dates.sort()

    for i in non_repeated_dates:
        count[str(i)] = {"total": dates.count(i), "type": issue_type}

    return count


f = open('result.json')

data = json.load(f)
f.close()

dates_created = []
dates_closed = []
count = {}

for issue in data['issues']:
    dates_created.append(issue['created_at'].split('T')[0].replace('-', ''))
    dates_closed.append(issue['closed_at'].split('T')[0].replace('-', ''))

print(dates_created)
print(dates_closed)

count = parse_dates(count, dates_created, "created")
print(count)
count = parse_dates(count, dates_closed, "closed")
print(count)

