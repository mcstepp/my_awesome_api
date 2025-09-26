# My Awesome API

A simple Python API built with FastAPI that includes API key authentication using Unkey. This project is for Unkey Deploy Demo. 

## Features

- Two endpoints: `/person` and `/status`
- API key authentication with Unkey
- OpenAPI specification generation
- Rate limiting and usage tracking

## Prerequisites

- Python 3.8+
- Unkey account and API key

## Installation

1. **Clone or download the project**
   ```bash
   cd my_awesome_api
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   UNKEY_ROOT_KEY=your_unkey_root_key_here
   ```

## Running the API

1. **Activate virtual environment** (if not already active)
   ```bash
   source venv/bin/activate
   ```

2. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

3. **API will be available at:**
   - API: `http://localhost:8000`
   - Interactive docs: `http://localhost:8000/docs`
   - OpenAPI spec: `http://localhost:8000/openapi.json`

## API Endpoints

### GET /person
Returns mock person data.

**Authentication:** Required

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com",
  "city": "New York"
}
```

### GET /status
Returns a boolean status.

**Authentication:** Required

**Response:**
```json
true
```

## Usage Examples

### With curl
```bash
# Test the person endpoint
curl -H "Authorization: Bearer your_api_key_here" http://localhost:8000/person

# Test the status endpoint
curl -H "Authorization: Bearer your_api_key_here" http://localhost:8000/status

# Pretty print JSON response
curl -H "Authorization: Bearer your_api_key_here" http://localhost:8000/person | jq
```

### Authentication
All endpoints require a valid API key in the Authorization header:
```
Authorization: Bearer your_api_key_here
```

## Development

The API automatically reloads when you make changes to the code (thanks to the `--reload` flag).

To generate a fresh OpenAPI specification:
```bash
python -c "from main import app; import json; from fastapi.openapi.utils import get_openapi; print(json.dumps(get_openapi(title=app.title, version=app.version, routes=app.routes), indent=2))" > openapi.json
```

## Project Structure

```
my_awesome_api/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (not in git)
├── .gitignore          # Git ignore rules
├── openapi.json        # Generated OpenAPI specification
├── venv/               # Virtual environment (not in git)
└── README.md           # This file
```