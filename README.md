[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/n4z4v0d)](https://t.me/n4z4v0d)
[![PyPI supported Python versions](https://img.shields.io/pypi/pyversions/better-automation.svg)](https://www.python.org/downloads/release/python-3116/)
[![works badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)  

![alt text](https://i.imgur.com/PDYwSJ9.png)

### Функционал  
+ Многопоточность
+ Привязка прокси к сессии
+ Авто-покупка предметов при наличии денег (enery boost, speed boost, click boost)
+ Рандомное время сна между кликами
+ Рандомное количество кликов за запрос

### data/config.py  
_**API_ID / API_HASH** - Данные платформы, с которой запускать сессию Telegram (сток - Android)  
**DELAY_BETWEEN_CLICK_RANGE** - Диапазон задержки между кликами (в секундах)  
**MIN_CLICKS_COUNT** - Минимальное количество кликов за один запрос (считается без множителя, т.е напр. при множителе x9: 1 клик будет равнятся 9 монетам, а не одной)  
**AUTO_BUY_ITEMS** - Вкл/откл автопокупки улучшений при наличии денег  
**SLEEP_BEFORE_BUY_MERGE** - Диапазон задержки между покупкой бустов (в секундах)_

# DONATE (_any evm_) - 0xDEADf12DE9A24b47Da0a43E1bA70B8972F5296F2
