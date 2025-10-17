from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime, timezone
import requests
import logging

logger =logging.getLogger(__name__)

def me(request):
    try:
        logger.info("Fetching cat fact from external API...")
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        data = response.json()
        cat_fact = data.get("fact","no cat fact available")

    except Exception as e:
        logger.error(f"Error fetching cat fact: {e}",exc_info=True)
        cat_fact = "Could not fetch cat fact at this time. Please try again later."
        
    result = {
        "status": "success",
        "user": {
            "email": "beatricegachigi@gmail.com",
            "name": "Beatrice Gachigi",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
        }

    logger.debug(f"Response: {result}")

    return JsonResponse(result)


    


    

