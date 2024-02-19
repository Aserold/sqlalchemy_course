from sqlalchemy import text, insert
from database import engine, async_engine, session_gen, async_session_gen, Base
from models import EmployeesOrm


class SyncORM:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        engine.echo = True
        Base.metadata.create_all(engine)
        engine.echo = True


    def insert_employees():
        with session_gen() as session:
            employee_bobr = EmployeesOrm(username='Bobr')
            employee_volk = EmployeesOrm(username='Volk')   
            session.add_all([employee_bobr, employee_volk])
            session.flush()
            session.commit()


class AsyncORM:
    @classmethod
    async def insert_data_async():
        async with async_session_gen() as session:
            employee_bobr = EmployeesOrm(username='Bobr')
            employee_volk = EmployeesOrm(username='Volk')
            session.add_all([employee_bobr, employee_volk])
            await session.commit()
