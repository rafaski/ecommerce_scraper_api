from fastapi import APIRouter, Request, Depends

from app.schemas import Output
from app.celery_app import run_crawler
from app.settings import TASK_DEFAULT_QUEUE
from app.auth import verify_api_key

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.get("/crawl")
async def crawl(request: Request, url: str, callback_url: str) -> Output:
    """
    Create a data scraping task. Provide supported product url and callback url.
    """
    run_crawler.apply_async(args=(url, callback_url), queue=TASK_DEFAULT_QUEUE)

    return Output(success=True, message="Task accepted")
