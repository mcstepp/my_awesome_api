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

### Option 1: Using Docker (Recommended)

1. **Build the Docker image**
   ```bash
   docker build -t my-awesome-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 my-awesome-api
   ```

3. **API will be available at:**
   - API: `http://localhost:8080`
   - Interactive docs: `http://localhost:8080/docs`
   - OpenAPI spec: `http://localhost:8080/openapi.json`

### Option 2: Local Development

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
curl -H "Authorization: Bearer your_api_key_here" http://localhost:8080/person

# Test the status endpoint
curl -H "Authorization: Bearer your_api_key_here" http://localhost:8080/status

# Pretty print JSON response
curl -H "Authorization: Bearer your_api_key_here" http://localhost:8080/person | jq
```

### Authentication
All endpoints require a valid API key in the Authorization header:
```
Authorization: Bearer your_api_key_here
```

## Development

The API automatically reloads when you make changes to the code (thanks to the `--reload` flag).

### OpenAPI Specification

The OpenAPI spec is automatically generated in YAML format (`openapi.yaml`) every time the application starts. This happens through a startup event handler in the FastAPI app.

If you need to manually regenerate it without starting the server:
```bash
python -c "from main import app; import yaml; yaml.dump(app.openapi(), open('openapi.yaml', 'w'), default_flow_style=False, sort_keys=False)"
```

## Project Structure

```
my_awesome_api/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── .dockerignore        # Docker ignore rules
├── .env                # Environment variables (not in git)
├── .gitignore          # Git ignore rules
├── openapi.yaml        # Generated OpenAPI specification
├── venv/               # Virtual environment (not in git)
└── README.md           # This file
```