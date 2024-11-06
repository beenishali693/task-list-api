from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime
from sqlalchemy import DateTime
from typing import Optional

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, default=None)
    is_complete: Mapped[bool] = mapped_column(default=False)

    def to_dict(self):
        task_as_dict = {
            "id" : self.id,
            "title" : self.title,
            "description": self.description,
            "is_complete": self.is_complete
        }
        return task_as_dict