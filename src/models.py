import datetime
from typing import Annotated
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_256
import enum


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.utcnow,
    )]

metadata_obj = MetaData()


# employees_table = Table(
#     'employees',
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('username', String)
# )


class EmployeesOrm(Base):
    __tablename__ = 'employees'

    id: Mapped[intpk]
    username: Mapped[str]


class Workload(enum.Enum):
    fulltime = 'fulltime'
    parttime = 'parttime'
    contract = 'contract'


class ResumesOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    username: Mapped[str_256]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id', ondelete='CASCADE'))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
