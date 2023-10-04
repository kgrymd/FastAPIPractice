from fastapi import APIRouter

router = APIRouter()

@router.put("/taskd/{task_id}/done")
async def mark_task_as_done():
    pass

@router.delete("/taskd/{task_id}/done")
async def unmark_task_as_done():
    pass