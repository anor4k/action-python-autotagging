import os
from pathlib import Path

from github import Github


def main():
    about = {}
    variable = os.environ["INPUT_VARIABLE"]
    with Path(os.environ["INPUT_PATH"]).open() as f:
        # If you have a simple variable assignment, you should use this as this prevents ImportErrors when you try to
        # imports packages that are not installed.
        if os.environ.get("INPUT_EXECUTE_ENTIRE_PATH", "0") == "0":
            line_assigning_the_variable = [line.strip() for line in f.readlines() if line.strip().startswith(variable)]
            if len(line_assigning_the_variable) != 1:
                raise ValueError(f"Found multiple lines starting with '{variable}'.")
            exec(line_assigning_the_variable[0], about)
        # If you compute the version, you should use this.
        else:
            exec(f.read(), about)

    prefix, suffix = os.environ["INPUT_PREFIX"], os.environ["INPUT_SUFFIX"]
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
    print(f"Created tag {version_tag}.")


if __name__ == "__main__":
    main()
