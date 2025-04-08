from typing import Annotated

from database.database import get_db_session

from fastapi import APIRouter, status, Depends, HTTPException

from shema.settings import Task
from repository.__init__ import TaskRepository
from depencies import get_task_repository


router = APIRouter(prefix='/task', tags=['task'])

@router.get(
    '/all',
    response_model=list[Task]
)
async def get_tasks(task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    result = task_repository.get_tasks()
    return result


@router.put(
    '/all',
    response_model=Task
)
async def create_task(task: Task,
                      task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    task_repository.create_task(task)
    return task

@router.delete(
    '/{task_id}'
)
async def delete_task(task_id: int,
                      task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    task_repository.delete_task(task_id)
    return {'message': 'task deleted'}


@router.patch(
'/{task_id}',
    response_model=Task
)
async def rename_task(task_id:int,
                      name: str,
                      task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    return task_repository.rename_task(task_id, name)