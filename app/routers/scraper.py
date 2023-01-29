from fastapi import APIRouter, Request

from app.schemas import Output
from app.celery_app import run_crawler

router = APIRouter()


@router.get("/crawl")
async def crawl(request: Request, url: str, callback_url: str) -> Output:
    """
    Request review data
    """
    run_crawler.apply_async(args=(url, callback_url), queue="test")

    return Output(success=True, message="Task accepted")


# @router.get("/results")
# async def results(request: Request) -> Output:
#     """
#     Get query results
#     """
#     return Output(success=True)
