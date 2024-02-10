from task_executor.db.models import user
from flask_seeder import FlaskSeeder
from task_executor import db, app


@app.route("/")
def hello_world():
    return db.one_or_404(db.select(user.User).filter_by(name="example"))

def main():
    seeder = FlaskSeeder()
    seeder.init_app(app, db)
    app.run(debug=True, host='127.0.0.1', port=5000)


if __name__ == '__main__':
   main()
