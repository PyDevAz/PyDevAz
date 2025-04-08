from repository.task import TaskRepository

from database.database import get_db_session


def get_task_repository() -> TaskRepository:
    dbSession = get_db_session()
    return TaskRepository(dbSession)
