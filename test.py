import argparse
from grimoirelab_perceval.perceval.backends.core.github import GitHub
from grimoirelab_perceval.perceval.backends.core.git import Git

lines = []


def get_commits(owner, repo):
    commits = 0

    repo_url = f'http://github.com/{owner}/{repo}.git'
    repo_dir = f'/tmp/{repo}.git'
    repo = Git(uri=repo_url, gitpath=repo_dir)

    for commit in repo.fetch():
        line = f"Commit: {commit['data']['commit'][0:7]} || \
            Author: {commit['data']['Author'].split('<')[0]} || \
            Files Changed: {len(commit['data']['files'])}\n" 
        #lines.append(line)
        commits += 1
    return commits


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
#get_commits(owner, repo)
count = 0
repo = GitHub(owner=owner, repository=repo, api_token=args.token)
for item in repo.fetch():
    if 'pull_request' in item['data']:
        kind = 'Pull request'
        pulls += 1
    else:
        kind = 'Issue'
        issues += 1
    
    # lines.append(f"{item['data']['number']}: {kind}\n")
    lines.append(f"{item['data']}\n")
    count += 1
    if count == 2:
        break

print(f"Repository > Commits: {commits} || Issues: {issues} || Pull Requests: {pulls}")

with open('result.json', 'w+') as writer:
    writer.writelines(lines)
    writer.close()
