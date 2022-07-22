import os
from pathlib import Path

from github import Github


def main():
    about = {}
    with Path(os.environ["INPUT_PATH"]).open() as f:
        exec(f.read(), about)

    prefix, suffix = os.environ["INPUT_PREFIX"], os.environ["INPUT_SUFFIX"]
    variable = os.environ["INPUT_VARIABLE"]
    version_tag = f"{prefix}{about[variable]}{suffix}"
    secret_token = os.environ["INPUT_TOKEN"]
    repository = os.environ["GITHUB_REPOSITORY"]

    print(f"Configuration: {version_tag=}, {repository=}, {len(secret_token)=}")

    g = Github(secret_token)
    repo = g.get_repo(repository)

    for tag in repo.get_tags():
        if tag.name == version_tag:
            return

    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{version_tag}", sha)


if __name__ == "__main__":
    main()
