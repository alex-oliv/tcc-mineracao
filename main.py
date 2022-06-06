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

    repo_url = f'http://github.com/{owner}/{repo}.git'
    repo_dir = f'/tmp/{repo}.git'
    repo = Git(uri=repo_url, gitpath=repo_dir)

    for commit in repo.fetch():
        line = f"Commit: {commit['data']['commit'][0:7]} || \
            Author: {commit['data']['Author'].split('<')[0]} || \
            Files Changed: {len(commit['data']['files'])}\n"
        # lines.append(line)
        commits += 1
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


def parse_dates(dates):
    count = {}

    non_repeated_dates = remove_duplicates(dates)
    non_repeated_dates.sort()

    for i in non_repeated_dates:
        count[str(i)] = dates.count(i)

    return count


issues = 0
pulls = 0
parser = argparse.ArgumentParser(
    description="Simple parser for GitHub issues and pull requests"
)
parser.add_argument("-t", "--token", '--nargs', nargs='+', help="GitHub token")
parser.add_argument("-r", "--repo", help="GitHub repository, as 'owner/repo'")
args = parser.parse_args()

(owner, repo) = args.repo.split('/')
commits = get_commits(owner, repo)
print(args.token)
count = 0
repo = GitHub(owner=owner, repository=repo, api_token=args.token)

dates_created = []
dates_closed = []
aux = []

for item in repo.fetch():
    if 'pull_request' in item['data']:
        pulls += 1
    else:
        #info['number'] = item['data']['number']
        # print("Number: ",info['number'])
        #info['creator'] = item['data']['user']['login']
        #info['state'] = item['data']['state']
        #info['labels'] = parse_arrays(item['data']['labels'], 'name')
        #info['assignees'] = len(parse_arrays(
            #item['data']['assignees'], 'login'))
        #info['comments'] = item['data']['comments']
        info['created_at'] = item['data']['created_at']
        date = info['created_at'].split('T')[0].replace('-', '')
        dates_created.append(date)
        info['closed_at'] = item['data']['closed_at']
        date = info['closed_at'].split('T')[0].replace('-', '')
        dates_closed.append(date)
        #result = json.dumps(info, indent=4)
        # lines.append(f"{result},")

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
    if count == 3:
        break

result = {}
result['issues'] = aux
lines.append(json.dumps(result))

print(
    f"Repository > Commits: {commits} || Issues: {issues} || Pull Requests: {pulls}")

with open('result.json', 'w+') as writer:
    # json.dump(lines, writer)
    writer.writelines(lines)
    writer.close()


created_dates = parse_dates(dates_created)
closed_dates = parse_dates(dates_closed)

# print(created_dates)
# print(closed_dates)
