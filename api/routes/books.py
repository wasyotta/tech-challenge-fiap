from fastapi import APIRouter, HTTPException, Query
from api.repositories.csv_repository import CsvRepository
from api.services.books_service import BooksService

router = APIRouter()
_service = BooksService(CsvRepository())

@router.get("/books")
def list_books(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=200),
    category: str | None = None
):
    items, total, total_pages = _service.list_books(page, limit, category)
    return {"page": page, "limit": limit, "total": total, "total_pages": total_pages, "items": items}

@router.get("/books/{book_id}")
def get_book(book_id: int):
    book = _service.get_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/books/search")
def search_books(title: str | None = None, category: str | None = None):
    return {"items": _service.search(title=title, category=category)}

@router.get("/books/top-rated")
def top_rated(limit: int = Query(10, ge=1, le=100)):
    df = _service.repo.load()
    df2 = df.sort_values(by=["rating", "price"], ascending=[False, True]).head(limit)
    return {"items": df2.to_dict(orient="records")}

@router.get("/books/price-range")
def price_range(min: float | None = None, max: float | None = None):
    df = _service.repo.load()
    if min is not None:
        df = df[df["price"] >= min]
    if max is not None:
        df = df[df["price"] <= max]
    return {"items": df.to_dict(orient="records")}
