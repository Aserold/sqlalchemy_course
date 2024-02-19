from sqlalchemy import select, text, insert, update
from database import engine, async_engine
from models_core import metadata_obj, employees_table


def get_123_sync():
    with engine.connect() as conn:
        res = conn.execute(text('SELECT 1,2,3 union select 4,5,6'))
        print(f'{res.all()}')


async def get_123_async():
    async with async_engine.connect() as connection:
        result = await connection.execute(text('SELECT 1,2,3 union select 4,5,6'))
        print(f'{result.all()=}')


class SyncCore:
    @staticmethod
    def create_tables():
        engine.echo = False
        metadata_obj.drop_all(engine)
        metadata_obj.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_employees():
        with engine.connect() as conn:
            # stmt = """INSERT INTO workers (username) VALUES 
            #     ('Jack'),
            #     ('Michael');"""
            stmt = insert(employees_table).values(
                [
                    {"username": "Jack"},
                    {"username": "Michael"},
                ]
            )
            conn.execute(stmt)
            conn.commit()
    
    @staticmethod
    def select_employees():
        with engine.connect() as conn:
            query = select(employees_table)
            result = conn.execute(query)
            employees = result.all()
            print(employees)

    @staticmethod
    def update_employee(employee_id: int = 2, new_username: str = 'Lev'):
        with engine.connect() as conn:
            # stmnt = text('UPDATE employees SET username=:username WHERE id=:id')
            # stmnt = stmnt.bindparams(username=new_username, id=employee_id)
            stmnt = (
                update(employees_table)
                .values(username=new_username)
                # .where(employees_table.c.id==employee_id)
                .filter_by(id=employee_id)
            )
            conn.execute(stmnt)
            conn.commit()


class AsyncCore:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(metadata_obj.drop_all())
            await conn.run_sync(metadata_obj.create_all())
