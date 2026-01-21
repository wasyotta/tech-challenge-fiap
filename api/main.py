from api.routes.stats import router as stats_router
from fastapi import FastAPI
from api.routes.health import router as health_router
from api.routes.categories import router as categories_router
from api.routes.books import router as books_router

app = FastAPI(
    title="Books Public API (Tech Challenge)",
    version="1.0.0",
    description="API pública baseada no dataset extraído de books.toscrape.com"
)

app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(categories_router, prefix="/api/v1", tags=["Categories"])
app.include_router(books_router, prefix="/api/v1", tags=["Books"])
app.include_router(stats_router, prefix="/api/v1", tags=["Stats"])

@app.get("/")
def root():
    return {"message": "OK - acesse /docs para Swagger"}
