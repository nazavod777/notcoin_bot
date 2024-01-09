from pathlib import Path

import aiosqlite
from TGConvertor.manager.sessions.pyro import PyroSession


async def new_validate(cls, path: Path) -> bool:
    try:
        async with aiosqlite.connect(path) as db:
            db.row_factory = aiosqlite.Row
            sql = "SELECT name FROM sqlite_master WHERE type='table'"
            async with db.execute(sql) as cursor:
                tables = {row["name"] for row in await cursor.fetchall()}

            if tables != set(cls.TABLES.keys()):
                return False

            for table, session_columns in cls.TABLES.items():
                sql = f'pragma table_info("{table}")'
                async with db.execute(sql) as cur:
                    columns = {row["name"] for row in await cur.fetchall()}
                    if "api_id" in columns:
                        columns.remove("api_id")
                    if session_columns != columns:
                        return False

    except aiosqlite.DatabaseError:
        return False

    return True


PyroSession.validate = classmethod(new_validate)
