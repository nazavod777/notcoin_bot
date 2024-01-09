import aiosqlite


async def on_startup_database() -> None:
    async with aiosqlite.connect(database='database/sessions.db') as db:
        await db.execute(sql="""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY,
            session_name TEXT,
            session_proxy TEXT
        );
        """)
        await db.commit()
