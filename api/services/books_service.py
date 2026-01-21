import math
from api.repositories.csv_repository import CsvRepository

class BooksService:
    def __init__(self, repo: CsvRepository):
        self.repo = repo

    def list_books(self, page: int, limit: int, category: str | None = None):
        df = self.repo.load()

        if category:
            df = df[df["category"].str.contains(category, case=False, na=False)]

        total = len(df)
        total_pages = max(1, math.ceil(total / limit))

        start = (page - 1) * limit
        end = start + limit
        items = df.iloc[start:end].to_dict(orient="records")

        return items, total, total_pages

    def get_by_id(self, book_id: int):
        df = self.repo.load()
        found = df[df["id"] == book_id]
        if found.empty:
            return None
        return found.iloc[0].to_dict()

    def search(self, title: str | None = None, category: str | None = None):
        df = self.repo.load()

        if title:
            df = df[df["title"].str.contains(title, case=False, na=False)]
        if category:
            df = df[df["category"].str.contains(category, case=False, na=False)]

        return df.to_dict(orient="records")

    def categories(self):
        df = self.repo.load()
        if df.empty:
            return []
        return sorted(df["category"].dropna().unique().tolist())
