import os
import pandas as pd

class CsvRepository:
    def __init__(self, csv_path: str = "data/books.csv"):
        self.csv_path = csv_path
        self._df = None

    def load(self) -> pd.DataFrame:
        if self._df is not None:
            return self._df

        if not os.path.exists(self.csv_path):
            self._df = pd.DataFrame(columns=[
                "id","title","price","rating","availability","category","image_url","product_page_url"
            ])
            return self._df

        df = pd.read_csv(self.csv_path)

        # Normalizações
        df["id"] = df["id"].astype(int)
        df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0.0)
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce").fillna(0).astype(int)

        self._df = df
        return self._df
