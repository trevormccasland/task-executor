from task_executor.db.models import User
from task_executor import repository, app, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def hello_world():
    item = repository.one_or_404(repository.select(User).filter_by(name="example"))
    return item.as_dict()


def main():
    app.run(debug=True, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
