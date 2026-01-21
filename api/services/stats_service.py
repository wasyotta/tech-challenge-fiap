from api.repositories.csv_repository import CsvRepository

class StatsService:
    def __init__(self, repo: CsvRepository):
        self.repo = repo

    def overview(self):
        df = self.repo.load()
        total = int(len(df))
        avg_price = float(df["price"].mean()) if total else 0.0

        rating_distribution = {}
        if total:
            counts = df["rating"].value_counts().sort_index()
            rating_distribution = {int(k): int(v) for k, v in counts.items()}

        return {
            "total_books": total,
            "average_price": round(avg_price, 2),
            "rating_distribution": rating_distribution
        }

    def categories(self):
        df = self.repo.load()
        if df.empty:
            return []

        grouped = df.groupby("category").agg(
            total_books=("id", "count"),
            avg_price=("price", "mean"),
            min_price=("price", "min"),
            max_price=("price", "max")
        ).reset_index()

        out = []
        for _, row in grouped.iterrows():
            out.append({
                "category": row["category"],
                "total_books": int(row["total_books"]),
                "avg_price": round(float(row["avg_price"]), 2),
                "min_price": round(float(row["min_price"]), 2),
                "max_price": round(float(row["max_price"]), 2),
            })
        return out
