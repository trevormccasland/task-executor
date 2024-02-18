from db.models import user, task
from flask_seeder import Seeder, Faker


class UserSeeder(Seeder):

    def run(self):
        faker = Faker(cls=user.User, init={"id": 1, "name": "example"})
        self.db.session.add(faker.create()[0])


class TaskSeeder(Seeder):

    def run(self):
        faker = Faker(cls=task.Task, init={"id": 1, "command": 'echo \\"hello\\"'})
        self.db.session.add(faker.create()[0])
