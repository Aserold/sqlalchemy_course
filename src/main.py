import asyncio
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

# from queries.core import create_tables, insert_data
from queries.orm import create_tables, insert_data, insert_data_async

create_tables()
# insert_data()
# asyncio.run(insert_data_async())
