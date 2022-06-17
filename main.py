import argparse
from datetime import datetime
import json
from grimoirelab_perceval.perceval.backends.core.github import GitHub
from grimoirelab_perceval.perceval.backends.core.git import Git

info = {}
lines = []
#
# python3 main.py -r ES2-UFPI/maltese -t


def get_commits(owner, repo):
    commits = 0
    count = 0
    lines = []

    repo_url = f'http://github.com/{owner}/{repo}.git'
    repo_dir = f'/tmp/{repo}.git'
    repo = Git(uri=repo_url, gitpath=repo_dir)

    for commit in repo.fetch():
        # line = f"Commit: {commit['data']['commit'][0:7]} || \
        #     Author: {commit['data']['Author'].split('<')[0]} || \
        #     Files Changed: {len(commit['data']['files'])}\n"
        commits += 1
        count += 1
        if count == 5:
            break
        lines.append(f"{commit}\n")

    return commits


def parse_arrays(arr, key):
    objects = []

    for item in arr:
        objects.append(item[key])

    return objects


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


def get_issues(owner, repo):
    issues = 0
    pulls = 0
    aux = []

    token = ['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']
    repo = GitHub(owner=owner, repository=repo, api_token=token)

    dates_created = []
    dates_closed = []

    for item in repo.fetch():
        if 'pull_request' in item['data']:
            pulls += 1
        else:
            info['created_at'] = item['data']['created_at']
            date = info['created_at'].split('T')[0].replace('-', '')
            dates_created.append(date)
            info['closed_at'] = item['data']['closed_at']
            date = info['closed_at'].split('T')[0].replace('-', '')
            dates_closed.append(date)

            labels = parse_arrays(item['data']['labels'], 'name')
            assignees = len(parse_arrays(
                item['data']['assignees'], 'login'))

            issue = {'number': item['data']['number'],
                        'creator': item['data']['user']['login'],
                        'state': item['data']['state'],
                        'labels': labels,
                        'assignees': assignees,
                        'comments': item['data']['comments'],
                        'created_at': item['data']['created_at'],
                        'closed_at': item['data']['closed_at']
                        }
            aux.append(issue)
            issues += 1

    result = {}
    result['issues'] = aux
    # lines.append(json.dumps(result))
    return json.dumps(result)

def filter_issues_by_dates(dates, begin=None, final=None):
    issues_by_dates = {}

    for key in dates:
        if(begin == None and final == None):
            issues_by_dates.update({key: dates[key]})
        elif(begin and final == None):
            if key >= begin:
                issues_by_dates.update({key: dates[key]})
        elif(begin == None and final):
            if key <= final:
                issues_by_dates.update({key: dates[key]})
        else:
            if key >= begin and key <= final:
                issues_by_dates.update({key: dates[key]})

    return issues_by_dates

def issues_dates(owner, repo, begin=None, final=None):
    data = json.loads(get_issues(owner, repo))
    dates_created = []
    dates_closed = []
    count = {}

    for issue in data['issues']:
        dates_created.append(issue['created_at'].split('T')[
                             0].replace('-', ''))
        dates_closed.append(issue['closed_at'].split('T')[0].replace('-', ''))

    parse_dates_same_day(count, dates_created, "created")
    parse_dates_same_day(count, dates_closed, "closed")

    #print(count)

    return filter_issues_by_dates(count, begin, final)


print(issues_dates('ES2-UFPI', 'maltese', '20201123', '20201215'))


