# services/mexc/app.py
from fastapi import FastAPI, HTTPException
import os
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/get_balance")
def get_balance(token: str = None):
    # Получаем API ключи из переменных окружения
    api_key = os.getenv("MEXC_API_KEY")
    secret_key = os.getenv("MEXC_SECRET_KEY")
    if not api_key or not secret_key:
        logger.error("API ключи MEXC не установлены")
        raise HTTPException(
            status_code=500, detail="Отсутствуют API ключи MEXC")

    try:
        # Пример запроса к Mexc (гипотетический endpoint; адаптируйте по документации)
        headers = {
            "Content-Type": "application/json",
            "apiKey": api_key,
            "apiSecret": secret_key
        }
        # Обратите внимание: настоящий endpoint может отличаться; см. документацию Mexc
        url = "https://www.mexc.com/open/api/v2/account/info"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Ошибка получения баланса MEXC: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка API MEXC: {e}")


