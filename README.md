# Consumer Attention Mapping System — Backend

FastAPI backend for the Consumer Attention Mapping System, providing authentication and store/zone/shelf/camera management APIs.

## Tech Stack
- Python 3.12, FastAPI, Uvicorn
- PostgreSQL, SQLAlchemy (ORM)
- JWT authentication (python-jose), bcrypt password hashing (passlib)

## Project Structure
## Setup Instructions

1. Create and activate a virtual environment:
2. Install dependencies:
3. Create a `.env` file in the project root with:
4. Run the server:
5. Visit the interactive API docs at `http://127.0.0.1:8000/docs`

## API Endpoints
- `POST /auth/register` — Register a new user
- `POST /auth/login` — Log in and receive a JWT token
- `GET/POST /stores` — List/create stores
- `GET/POST /zones` — List/create zones
- `GET/POST /shelves` — List/create shelves
- `GET/POST /cameras` — List/create cameras
