import asyncio
from os import listdir
from os import mkdir
from os.path import exists
from sys import stderr

from loguru import logger

from core import create_sessions, start_farming
from database import on_startup_database
from utils import monkeypatching

logger.remove()
logger.add(stderr, format='<white>{time:HH:mm:ss}</white>'
                          ' | <level>{level: <8}</level>'
                          ' | <cyan>{line}</cyan>'
                          ' - <white>{message}</white>')


async def main() -> None:
    await on_startup_database()

    match user_action:
        case 1:
            await create_sessions()

            logger.success('Сессии успешно добавлены')

        case 2:
            tasks: list = [
                asyncio.create_task(coro=start_farming(session_name=current_session_name))
                for current_session_name in session_files
            ]

            await asyncio.gather(*tasks)

        case _:
            logger.error('Действие выбрано некорректно')


if __name__ == '__main__':
    if not exists(path='sessions'):
        mkdir(path='sessions')

    session_files: list[str] = [current_file[:-8] if current_file.endswith('.session')
                                else current_file for current_file in listdir(path='sessions')]

    logger.info(f'Обнаружено {len(session_files)} сессий')

    user_action: int = int(input('\n1. Создать сессию'
                                 '\n2. Запустить бота с существующих сессий'
                                 '\nВыберите ваше действие: '))
    print()

    try:
        import uvloop

        uvloop.run(main())

    except ModuleNotFoundError:
        asyncio.run(main())

    input('\n\nPress Enter to Exit..')
