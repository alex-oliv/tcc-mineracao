from datetime import datetime
import json
from flask import Flask
from grimoirelab_perceval.perceval.backends.core.github import GitHub
from grimoirelab_perceval.perceval.backends.core.git import Git


app = Flask(__name__)


@app.route('/')
def show_home():
    return "<h1>Flask executando...</h1>"


@app.route('/info/<owner>/<repo>')
def show(owner, repo):
    result = get_issues(owner, repo)
    return result


@app.route('/info/issues-dates/<owner>/<repo>')
def show_issues(owner, repo):
    result = issues_dates(owner, repo)
    return result


@app.route('/info/issues-authors/<owner>/<repo>')
def show_issues_authors(owner, repo):
    result = issues_authors(owner, repo)
    return result


@app.route('/info/commits/<owner>/<repo>')
def show_total_commits(owner, repo):
    result = get_commits(owner, repo)
    return result


###############################


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


def parse_dates(count, dates, issue_type):
    non_repeated_dates = remove_duplicates(dates)
    non_repeated_dates.sort()

    for i in non_repeated_dates:
        count[str(i)] = {"total": dates.count(i), "type": issue_type}


def formatCommitDate(date):
    clear_date = datetime.strptime(date, '%c %z')

    return str(clear_date).split(' ')[0].replace('-', '')


def get_commits(owner, repo):
    aux = []
    date_commits = []

    repo_url = f'http://github.com/{owner}/{repo}.git'
    repo_dir = f'/tmp/{repo}.git'
    repo = Git(uri=repo_url, gitpath=repo_dir)

    for commit in repo.fetch():
        date = formatCommitDate(commit['data']['CommitDate'])
        date_commits.append(date)

        author = commit['data']['Author'].split(' <')[0]

        info = {date: {'author': author,
                       'files_changed': len(commit['data']['files'])
                    }
                }
        aux.append(info)

    
    result = {}
    result['commits'] = aux
    lines = []
    lines.append(json.dumps(result))
    
    with open('result3.json', 'w+') as writer:
        writer.writelines(lines)
        writer.close()
        return json.dumps(result)


def get_issues(owner, repo):
    issues = 0
    pulls = 0
    aux = []

    token = ['']
    repo = GitHub(owner=owner, repository=repo, api_token=token)
    for item in repo.fetch():
        if 'pull_request' in item['data']:
            pulls += 1
        else:
            labels = parse_arrays(item['data']['labels'], 'name')
            assignees = len(parse_arrays(
                item['data']['assignees'], 'login'))

            aux.append({'number': item['data']['number'],
                        'creator': item['data']['user']['login'],
                        'state': item['data']['state'],
                        'labels': labels,
                        'assignees': assignees,
                        'comments': item['data']['comments'],
                        'created_at': item['data']['created_at'],
                        'closed_at': item['data']['closed_at']
                        })
            issues += 1

    result = {}
    result['issues'] = aux
    return json.dumps(result)


def issues_dates(owner, repo):
    data = json.loads(get_issues(owner, repo))
    dates_created = []
    dates_closed = []
    count = {}

    for issue in data['issues']:
        dates_created.append(issue['created_at'].split('T')[
                             0].replace('-', ''))
        dates_closed.append(issue['closed_at'].split('T')[0].replace('-', ''))

    print(dates_created)
    print(dates_closed)

    parse_dates(count, dates_created, "created")
    parse_dates(count, dates_closed, "closed")

    return count


def issues_authors(owner, repo):
    data = json.loads(get_issues(owner, repo))
    creators = []
    count = {}

    for issue in data['issues']:
        creators.append(issue['creator'])

    non_repeated_creators = remove_duplicates(creators)
    non_repeated_creators.sort()

    for i in non_repeated_creators:
        count[str(i)] = creators.count(i)

    return count
