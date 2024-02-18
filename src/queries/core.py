from sqlalchemy import text, insert
from database import engine, async_engine
from models import metadata_obj, employees_table


def get_123_sync():
    with engine.connect() as conn:
        res = conn.execute(text('SELECT 1,2,3 union select 4,5,6'))
        print(f'{res.all()}')


async def get_123_async():
    async with async_engine.connect() as connection:
        result = await connection.execute(text('SELECT 1,2,3 union select 4,5,6'))
        print(f'{result.all()=}')


def create_tables():
    engine.echo = False
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)
    engine.echo = True


def insert_data():
    with engine.connect() as conn:
        # stmt = """INSERT INTO employees (username) VALUES
        #     ('Bobr'),
        #     ('Volk');"""
        stmnt = insert(employees_table).values(
            [
                {'username': 'Bobr'},
                {'username': 'Volk'},
            ]
        )
        conn.execute(stmnt)
        conn.commit()
