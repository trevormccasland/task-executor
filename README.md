# Task Executor
Run your tasks on a remote or local host

## Design Sketch

```
        +-----------------------------------+                  +-------------+
        |                                   |                  |             |
        |                                   |          +-------> host 1      |
        |       +-----------+               |          |       |             |
        |       |           |               |          |       +-------------+
        |       | flask     |     +---------+          |
        |       |  api      |     |scheduler|          |
        |       |           |     |* filter |          |        +-------------+
        |       +--+------+-+     |* weights+------------------->             |
        |          |      |       +---+-----+          |        | host 2      |
        |  +-------+----+ |           ^     |          |        |             |
        |  |            | |           |     |          |        +-------------+
        |  | sqlAlchemy | |    +---------+  |          |            ....
        |  |            | +----> redis|py|  |          |       +--------------+
        +--+----+-------+------------+------+          |       |              |
                |                    |                 +------>+  host n      |
                |                    |                         |              |
                |                    |                         +--------------+
                |                    |
                |                    |
                |                    |
+---------------+-+                  |
|                 |                 ++-------------+
|                 |                 |              |
|                 |                 |  redis queue |
|    postgres     |                 |  * pending   |
|   * Users       |                 |    executions|
|   * Tasks       |                 |              |
|   * History     |                 |              |
|   * Target      |                 |              |
|                 |                 |              |
+-----------------+                 +--------------+

```

## Dev Setup

### MacOS
Install pipx
```bash
brew install pipx
pipx ensurepath
```

Open a new terminal and install poetry
```
pipx --pip-args '--trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi python.org --trusted-host github.com' install poetry
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

### Windows
First make sure you are using python 3.11 or above. Update your path and confirm the python version using your terminal. You may have to restart if you are upgrading and modifying your path.

Install pipx
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Install poetry
```bash
python3 -m pipx install poetry
```

Get pipx location
```bash
python3 -m pip show pipx
```

Find the location output, add that to your windows system path, and restart
```bash
Location: C:\Users\trevo\AppData\Local\Programs\Python\Python312\Lib\site-packages
```

After pipx is added to your path you can just use it without calling python3.
Install poetry
```bash
pipx install poetry
```

Use poetry to install the app
```bash
poetry install
```

#### postgres setup
Install pgadmin https://www.postgresql.org/ftp/pgadmin/pgadmin4/v8.2/windows/
Create a user named task_executor, give it all permissions, and give it the password secret
Create a database named task-executor and assign the owner as task_executor

Run the app
```bash
poetry run task-executor
```