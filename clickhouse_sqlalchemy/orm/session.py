from typing import Union, Type, overload, Literal

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine

from .query import Query


@overload
def make_session(engine: Engine, is_async: Literal[False] = False) -> Session: ...


@overload
def make_session(engine: AsyncEngine, is_async: Literal[True]) -> AsyncSession: ...


def make_session(engine: Union[Engine, AsyncEngine], is_async: bool = False) -> Union[Session, AsyncSession]:
    session_class: Union[Type[Session], Type[AsyncSession]] = Session
    if is_async:
        session_class = AsyncSession

    factory = sessionmaker(bind=engine, class_=session_class)

    return factory(query_cls=Query)
