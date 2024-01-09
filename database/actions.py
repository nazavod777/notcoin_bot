import aiosqlite


async def add_session(session_name: str,
                      session_proxy: str = '') -> None:
    async with aiosqlite.connect(database='database/sessions.db') as db:
        await db.execute(sql='INSERT INTO sessions (session_name, session_proxy) VALUES (?, ?)',
                         parameters=(session_name, session_proxy))
        await db.commit()


async def get_session_proxy_by_name(session_name: str) -> str | None:
    async with aiosqlite.connect(database='database/sessions.db') as db:
        async with db.execute(sql='SELECT session_proxy FROM sessions WHERE session_name = ?',
                              parameters=(session_name,)) as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None
