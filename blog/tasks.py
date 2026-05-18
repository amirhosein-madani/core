# tasks.py
from celery import shared_task
import requests
from django.core.cache import cache


@shared_task
def get_brsapi():
    """
    task for get data from api and caching
    """

    cache_key = "brsapi"
    url = (
        "https://Api.BrsApi.ir/Tsetmc/AllSymbols.php?"
        "key=BGlsBBFzZHtKVXmNkQ1GVgtiizCX6g3g"
    )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36 OPR/106.0.0.0"
        ),
        "Accept": "application/json, text/plain, */*",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            cache.set(cache_key, data, 60 * 20)
            return {"success": True, "message": "data cached "}
        else:
            return {"success": False, "error": f"Status code {response.status_code}"}

    except Exception as e:
        return {"success": False, "error": str(e)}
