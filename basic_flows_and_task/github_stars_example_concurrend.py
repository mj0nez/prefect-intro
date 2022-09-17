from prefect import flow, task
import httpx

@task(retries=3)
def get_stars(repo):
    url = f"https://api.github.com/repos/{repo}"
    count = httpx.get(url).json()["stargazers_count"]
    print(f"{repo} has {count} stars!")

@flow()
def github_stars(repos):
    for repo in repos:
        get_stars.submit(repo)

# call the flow!
if __name__ == "__main__":
    github_stars(["PrefectHQ/Prefect", "PrefectHQ/prefect-aws",  "PrefectHQ/prefect-dbt"])
