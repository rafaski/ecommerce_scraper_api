from fastapi import FastAPI

from app.routers.scraper import router as scraper_router

description = """
## Ecommerce Scraper API ##

An E-commerce scraper allows you to scrape business info from google reviews.

...
"""

app = FastAPI(
    title="E-commerce Scraper API",
    docs_url="/",
    description=description
)

app.include_router(scraper_router)
