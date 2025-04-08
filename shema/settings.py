from pydantic import BaseModel, model_validator

class Task(BaseModel):
    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int


@model_validator(mode='after')
def check_name_or_pc_is_not_null(self):
    if self.name is None and self.pomdoro_count is None:
        raise ValueError('name and pomodoro_vount must be provided')
    return self
