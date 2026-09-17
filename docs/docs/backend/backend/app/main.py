from fastapi import FastAPI

app = FastAPI(
    title="MineTrack",
    description="Mining fleet, ROM movement, stockpile intelligence and material genealogy platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "MineTrack",
        "version": "0.1.0",
        "status": "online",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "minetrack-api",
    }
