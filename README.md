# Stupid Wallet API

Данный репозиторий создан для API @stupidwallet_bot

Документация находится в "wiki" [репозитория](https://github.com/penggrin12/stupidwalletapi/)

Для установки на iOS установите git и bash, 
а затем инициализируйте "bash iosinstall.sh".

пример использования в директории tests.

# Пример кода
```python
import asyncio
import stupidwalletapi

swapi = stupidwalletapi.StupidWalletAPI("YOUR_TOKEN")  # заменить на токен из @stupidwallet_bot

async def main():
    cheque = await swapi.create_cheque(stupidwalletapi.WAV_COIN, 1)  # создание чека
    print(cheque.id)  # вывод идентификатора чека

asyncio.run(main())
```



