from json import loads

import aiofiles
from aiofiles.ospath import exists
from loguru import logger


def get_value(file_json: dict,
                    *keys) -> str | None:
    for key in keys:
        if key in file_json:
            return file_json[key]
    return None


async def read_session_json_file(session_name: str) -> dict:
    file_path: str = f'sessions/{session_name}.json'
    result_dict: dict = {}

    try:
        if not await exists(file_path):
            return result_dict

        async with aiofiles.open(file=file_path,
                                 mode='r',
                                 encoding='utf-8') as file:
            file_json: dict = loads(await file.read())

        result_dict: dict = {
            'api_id': get_value(file_json, 'api_id', 'app_id', 'apiId', 'appId'),
            'api_hash': get_value(file_json, 'api_hash', 'app_hash', 'apiHash', 'appHash'),
            'device_model': get_value(file_json, 'deviceModel', 'device'),
            'system_version': get_value(file_json, 'systemVersion', 'system_version', 'appVersion', 'app_version'),
            'app_version': get_value(file_json, 'appVersion', 'app_version'),
            'lang_code': get_value(file_json, 'lang_pack', 'langCode', 'lang'),
            'system_lang_code': get_value(file_json, 'system_lang_pack', 'systemLangCode', 'systemLangPack')
        }

    except Exception as error:
        logger.error(f'{session_name} | Ошибка при чтении .json файла: {error}')

    return result_dict
