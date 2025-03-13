from fastapi import FastAPI, HTTPException
from typing import Optional
import os
import logging
from dotenv import load_dotenv

# Важно! Импортируем Client из pybitget.client
from pybitget.client import Client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()

app = FastAPI()

@app.get("/get_balance")
def get_balance(
    token: Optional[str] = None,
    api_key: Optional[str] = None,
    secret_key: Optional[str] = None,
    passphrase: Optional[str] = None
):
    # Если параметры не переданы через query, берем из переменных окружения
    if not api_key:
        api_key = os.getenv("BITGET_API_KEY")
    if not secret_key:
        secret_key = os.getenv("BITGET_SECRET_KEY")
    if not passphrase:
        passphrase = os.getenv("BITGET_PASSPHRASE")

    if not api_key or not secret_key or not passphrase:
        logger.error("API ключи Bitget или passphrase не установлены")
        raise HTTPException(status_code=500, detail="Отсутствуют API ключи Bitget или passphrase")

    try:
        # Создаем экземпляр клиента
        client = Client(api_key, secret_key, passphrase)
        # Пример вызова метода для получения баланса:
        # Проверяйте, какой метод реально возвращает баланс.
        # Здесь, например, mix_get_accounts(...) для USDT-маржинальных контрактов.
        balance_info = client.mix_get_accounts(productType="umcbl")
        return balance_info
    except Exception as e:
        logger.error(f"Ошибка обращения к API Bitget: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка API Bitget: {e}")
