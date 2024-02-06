# Task Executor
Run your tasks on a remote or local host

## Dev Setup

#### MacOS
Install pipx
```bash
brew install pipx
pipx ensurepath
```

Open a new terminal and install poetry
```
pipx --pip-args '--trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi python.org --trusted-host github.com' poetry
```
Configure poetry
```bash
poetry source add fpho https://files.pythonhosted.org
poetry config certificates.fpho.cert false
```

Install xattr
```bash
pipx install --pip-args '--trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host github.com' xattr
```

Install requirements with poetry
```bash
poetry install
```

Run the app
```bash
poetry run task-executor
```