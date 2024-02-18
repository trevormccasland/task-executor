from task_executor import login_manager, repository
from task_executor.db.models import User


@login_manager.user_loader
def get_user(id: int):
    return repository.query.get(User, id)
