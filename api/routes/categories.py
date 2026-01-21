from fastapi import APIRouter
from api.repositories.csv_repository import CsvRepository
from api.services.books_service import BooksService

router = APIRouter()
_service = BooksService(CsvRepository())

@router.get("/categories")
def categories():
    return {"categories": _service.categories()}
