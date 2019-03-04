from github import Github

g = Github("自己申请的Token")
repo = g.get_repo('bitcoin/bitcoin')
stargazers = repo.get_stargazers_with_dates()
for people in stargazers:
    print(people.starred_at)
    print(people.user)