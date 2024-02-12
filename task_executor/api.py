from task_executor.db.models import user
from task_executor import db_integration, app


@app.route("/")
def hello_world():
    item = db_integration.one_or_404(db_integration.select(user.User).filter_by(name="example"))
    return item.as_dict()

def main():
    app.run(debug=True, host='127.0.0.1', port=5000)


if __name__ == '__main__':
   main()
