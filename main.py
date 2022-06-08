import argparse
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

    with open('result-git.json', 'w+') as writer:
        writer.writelines(lines)
        writer.close()

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


def parse_dates(count, dates, issue_type):
    non_repeated_dates = remove_duplicates(dates)
    non_repeated_dates.sort()

    for i in non_repeated_dates:
        count[str(i)] = {"total": dates.count(i), "type": issue_type}

    return count


def built_json():
    issues = 0
    pulls = 0
    parser = argparse.ArgumentParser(
        description="Simple parser for GitHub issues and pull requests"
    )
    parser.add_argument("-t", "--token", '--nargs',
                        nargs='+', help="GitHub token")
    parser.add_argument(
        "-r", "--repo", help="GitHub repository, as 'owner/repo'")
    args = parser.parse_args()

    (owner, repo) = args.repo.split('/')
    # commits = get_commits(owner, repo)
    repo = GitHub(owner=owner, repository=repo, api_token=args.token)

    aux = []
    count = 0

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

        count += 1
        if count == 5:
            break
        # lines.append(f"{item}\n")

    result = {}
    result['issues'] = aux
    lines.append(json.dumps(result))
    dadad = 1
    # print(
    #     f"Repository > Commits: {dadad} || Issues: {issues} || Pull Requests: {pulls}")

    with open('result.json', 'w+') as writer:
        writer.writelines(lines)
        writer.close()

    # created_dates = parse_dates(dates_created)
    # closed_dates = parse_dates(dates_closed)
    return json.dumps(result)
    # print(created_dates)
    # print(closed_dates)


data = json.loads(built_json())
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
