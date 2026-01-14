import requests
from loguru import logger

def get_klines(symbol, interval="1h", limit=800):
    url = "https://fapi.binance.com/fapi/v1/klines"
    params = {
    "symbol": symbol,
    "interval": interval,
    "limit": limit
    }
    r = requests.get(url, params=params, timeout=10)
    #r.reverse()
    return r.json()

def get_binance_futures_tickers() -> list[str]:
    """
    Отримує список усіх активних ф'ючерсних тикерів (USDT-M) з біржі Binance.

    Returns:
        List[str]: Список тикерів (наприклад ['BTCUSDT', 'ETHUSDT', ...])
                  або порожній список у разі помилки.
    """
    url = "https://fapi.binance.com/fapi/v1/exchangeInfo"

    try:
        logger.debug("Запитуємо список ф'ючерсних тикерів з Binance...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        symbols = data.get("symbols", [])
        active_tickers = []

        for symbol_info in symbols:
            # Торгується + USDT маржа + perpetual
            if (
                symbol_info.get("status") == "TRADING"
                and symbol_info.get("contractType") == "PERPETUAL"
                and symbol_info.get("quoteAsset") == "USDT"
            ):
                active_tickers.append(symbol_info["symbol"])

        logger.debug(f"Отримано {len(active_tickers)} активних ф'ючерсних тикерів Binance")
        return active_tickers

    except requests.exceptions.Timeout:
        logger.error("Таймаут при запиті до Binance API")
    except requests.exceptions.ConnectionError:
        logger.error("Помилка з'єднання з Binance API")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP помилка Binance API: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Помилка запиту Binance API: {e}")
    except Exception as e:
        logger.error(f"Неочікувана помилка: {e}")

    return []