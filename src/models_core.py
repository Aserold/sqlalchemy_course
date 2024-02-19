import datetime
import enum
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, MetaData, String, Table, text, Enum


class Workload(enum.Enum):
    fulltime = 'fulltime'
    parttime = 'parttime'
    contract = 'contract'


metadata_obj = MetaData()

employees_table = Table(
    "employees",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)

resumes_table = Table(
    "resumes",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("title", String(256)),
    Column("compensation", Integer, nullable=True),
    Column("workload", Enum(Workload)),
    Column("employee_id", ForeignKey("employees.id", ondelete="CASCADE")),
    Column("created_at", TIMESTAMP,server_default=text("TIMEZONE('utc', now())")),
    Column("updated_at", TIMESTAMP,server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow),
)

vacancies_table = Table(
    "vacancies",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("compensation", Integer, nullable=True),
)

vacancies_replies_table = Table(
    "vacancies_replies",
    metadata_obj,
    Column("resume_id", ForeignKey("resumes.id", ondelete="CASCADE"), primary_key=True),
    Column("vacancy_id", ForeignKey("vacancies.id", ondelete="CASCADE"), primary_key=True),
)