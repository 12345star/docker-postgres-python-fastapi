import asyncio
from app.core.database import init_db

if __name__ == "__main__":
    asyncio.run(init_db())

# levanta solo el contenedor. docker compose up --build -d
# hacerlo manual correr la base de datos. docker compose run web python init_db.py 

# correr todo  docker compose up --build 
