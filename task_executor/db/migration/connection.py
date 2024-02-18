from sqlalchemy import create_engine


class DBConnection(object):
    def __init__(self, connection_url, connection=None):
        self.connection = connection
        self.connection_url = connection_url
        self.new_engine = False

    def __enter__(self):
        self.new_engine = self.connection is None
        if self.new_engine:
            self.engine = create_engine(
                "postgresql+pg8000://task_executor:secret@localhost:5432/task-executor",
                isolation_level="REPEATABLE READ",
            )
            self.connection = self.engine.connect()
        return self.connection

    def __exit__(self):
        if self.new_engine:
            try:
                self.connection.close()
            finally:
                self.engine.dispose()
