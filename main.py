from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils.coordinator import analyze_city
from app.simulation import simulate_city

# -------------------------
# Create FastAPI app FIRST
# -------------------------
app = FastAPI(title="AI Smart City Operations API")

# -------------------------
# CORS Middleware (AFTER app creation)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Routes
# -------------------------

@app.post("/analyze-city")
def analyze_city_endpoint(payload: dict):
    return analyze_city(payload)


@app.post("/simulate")
def simulate_city_endpoint(payload: dict):
    return simulate_city(payload)
