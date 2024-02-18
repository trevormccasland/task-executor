from task_executor.db.models import User
from task_executor import repository, app
from flask_login import current_user, login_user
from flask import request


@app.route("/login")
def login():
    if current_user.is_authenticated:
        return "Already Authenticated"
    user_id = request.args.get("id")
    user = repository.one_or_404(repository.select(User).filter_by(id=user_id))
    return "Login Succesful"


@app.route("/")
def hello_world():
    item = repository.one_or_404(repository.select(User).filter_by(name="example"))
    return item.as_dict()


def main():
    app.run(debug=True, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
