from fastapi import APIRouter
from api.repositories.csv_repository import CsvRepository

router = APIRouter()
_repo = CsvRepository()

@router.get("/health")
def health():
    df = _repo.load()
    return {"status": "ok", "dataset_loaded": len(df) > 0, "total_books": int(len(df))}
