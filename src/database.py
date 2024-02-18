import asyncio
from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, String, create_engine, text
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)


session_gen = sessionmaker(engine)
async_session_gen = async_sessionmaker(async_engine)

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }
