from fastapi import APIRouter
from api.repositories.csv_repository import CsvRepository
from api.services.stats_service import StatsService

router = APIRouter()
_service = StatsService(CsvRepository())

@router.get("/stats/overview")
def overview():
    return _service.overview()

@router.get("/stats/categories")
def stats_categories():
    return {"items": _service.categories()}
