from fastapi import FastAPI
from app.api.v1.api_v1 import router
from starlette.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://library-fronted.onrender.com"],  # Permite solicitudes desde esta URL (cambia si usas otro puerto o dominio)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los headers
)


app.include_router(router, prefix="/api/v1")
