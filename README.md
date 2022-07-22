# 🐍 Python Auto Tagging

Note: Credits go to @samamorgan for creating the first version.
This action will read a python version file and compare the version variable to the project's known tags. If a corresponding tag does not exist, it will be created.

## Usage

The following is an example `.github/workflows/main.yml` that will execute when a `push` to the `master` branch occurs.

### Example workflow

```yaml
name: 🐍 Auto Version Tag

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
        uses: Jorricks/action-python-autotagging@1.0.1

        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          path: src/your_package/__init__.py
          variable: __version__
```

### Inputs

| Input               | Required | Description                                                                     |
|---------------------|----------|---------------------------------------------------------------------------------|
| token               | Required | Github token to create the tag                                                  |
| path                | Required | Path to version file                                                            |
| variable            | Required | Variable name containing version information                                    |
| prefix              | Optional | Prefix to add to the version tag                                                |
| suffix              | Optional | Suffix to add to the version tag                                                |
| execute_entire_path | Optional | Whether to execute the entire file or just the list that starts with 'variable' |

By default `execute_entire_path=0`. This is perfect for when you define your variable with a simple `__version__==0.0.0`. However, if you compute your version inside the file, you should set `execute_entire_path=1` and make sure you installed any possible imports.

## Configuration

The `GITHUB_TOKEN` must be passed in. You don't need to setup anything for this variable, it will automatically be created. The only thing you need to make sure of is that you have your `Workflow permissions` set to the standard value of `Read and write permissions`, or, that you define the permissions in the workflow as [mentioned here](https://docs.github.com/en/actions/using-jobs/assigning-permissions-to-jobs).

```yaml
- uses: Jorricks/action-python-autotagging@1.0.1
  with:
    path: package/__version__.py
    variable: __version__
    github_token: ${{ secrets.GITHUB_TOKEN }}
```

**DO NOT MANUALLY ENTER YOUR TOKEN.** If you put the actual token in your workflow file, you'll make it accessible (in plaintext) to anyone who ever views the repository (it will be in your git history).
