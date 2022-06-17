import json


f = open('result2.json')

data = json.load(f)
f.close()


def count_issues(date, key, count):
    if not count.__contains__(date[key]['author']):
        count.update({date[key]['author']: date[key]['files_changed']})
    else:
        files = count.get(date[key]['author'])
        total_files = date[key]['files_changed'] + files
        count.update({date[key]['author']: total_files})

