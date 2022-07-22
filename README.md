# Python Container Action Template

This action will read a python version file and compare the version variable to the project's known tags. If a corresponding tag does not exist, it will be created.

## Usage

The following is an example `.github/workflows/main.yml` that will execute when a `push` to the `master` branch occurs.

### Example workflow

```yaml
name: Python 🐍 Auto Version Tag

on:
  push:
    branches:
      - main
    paths:
      - 'src/your_package/__init__.py'

jobs:
  tag:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Version tag
        uses: Jorricks/action-autotag-python@master

        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          path: src/your_package/__init__.py
          variable: __version__
```

### Inputs

| Input    | Required | Description                                  |
| -------- | -------- | -------------------------------------------- |
| token    | Required | Github token to create the tag               |
| path     | Required | Path to version file                         |
| variable | Required | Variable name containing version information |
| prefix   | Optional | Prefix to add to the version tag             |
| suffix   | Optional | Suffix to add to the version tag             |

## Configuration

The `GITHUB_TOKEN` must be passed in. You don't need to setup anything for this variable, it will automatically be created. The only thing you need to make sure of is that you have your `Workflow permissions` set to the standard value of `Read and write permissions`, or, that you define the permissions in the workflow as [mentioned here](https://docs.github.com/en/actions/using-jobs/assigning-permissions-to-jobs).

```yaml
- uses: Jorricks/action-autotag-python@master
  with:
    path: package/__version__.py
    variable: __version__
    github_token: ${{ secrets.GITHUB_TOKEN }}
```

**DO NOT MANUALLY ENTER YOUR TOKEN.** If you put the actual token in your workflow file, you'll make it accessible (in plaintext) to anyone who ever views the repository (it will be in your git history).
