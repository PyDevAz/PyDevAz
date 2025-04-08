from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from database import Tasks, get_db_session, Categories
from shema.settings import Task

class TaskRepository():
    def __init__(self, dbSession: Session):
        self.dbSession = dbSession


    def get_tasks(self):
        with self.dbSession()as session:
            task: list[Tasks] = session.execute(select(Tasks)).scalars().all()

            return task


    def get_task(self, task_id: int) -> Tasks | None:
        with self.dbSession() as session:
            task: Tasks = session.execute(select(Tasks).where(Tasks.id == task_id)).scalar_one_or_none()
            return task


    def create_task(self, task: Task) -> None:
        with self.dbSession() as session:
            task_model = Tasks(name=task.name, pomodoro_count=task.pomodoro_count, category_id=task.category_id)
            session.add(task_model)
            session.commit()


    def delete_task(self, task_id: int):
        with self.dbSession() as session:
            session.execute(delete(Tasks).where(Tasks.id == task_id))
            session.commit()

    def rename_task(self, task_id: int, task_name: str):
        querry = update(Tasks).where(Tasks.id == task_id).values(name=task_name).returning(Tasks.id)
        with self.dbSession() as session:
            task_id: int = session.execute(querry).scalar_one_or_none()
        return self.get_task(task_id)
