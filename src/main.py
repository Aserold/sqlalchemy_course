import asyncio
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.core import SyncCore, AsyncCore
from queries.orm import SyncORM

SyncORM.create_tables()
SyncORM.insert_employees()
SyncCore.select_employees()
SyncCore.update_employee()
SyncCore.select_employees()
