from db.models import user
from flask_seeder import Seeder, Faker

class UserSeeder(Seeder):

    def run(self):
        faker = Faker(
            cls=user.User,
            init={
                "id": 1,
                "name": "example"
            }
        )
        self.db.session.add(faker.create()[0])