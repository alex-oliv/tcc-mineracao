import json


f = open('result3.json')

data = json.load(f)
f.close()


def remove_duplicates(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)

    return result


def parse_dates(count, dates):
    non_repeated_dates = remove_duplicates(dates)
    non_repeated_dates.sort()

    for i in non_repeated_dates:
        count[str(i)] = {"total": dates.count(i)}


total = 0
commit_dates = []
for i in data['commits']:
    for key in i:
        commit_dates.append(key)


print(f'Total de commits: {total}')
print(len(data['commits']))


count = {}
parse_dates(count, commit_dates)

print(count)

# {
#       "20201207": {
#         "author": "Jo\u00e3o Pedro Patrocinio ",
#         "files_changed": 1
#       }
#     },
#     {
#       "20201207": {
#         "author": "Jo\u00e3o Pedro Patrocinio ",
#         "files_changed": 1
#       }
#     },
#     {
#       "20201207": {
#         "author": "Jo\u00e3o Pedro Patrocinio ",
#         "files_changed": 1
#       }
#     },
