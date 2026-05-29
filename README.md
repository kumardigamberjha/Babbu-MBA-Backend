# MBA HUB Backend

A Django-based REST API backend configured using [uv](https://github.com/astral-sh/uv).

## Getting Started

Make sure you have `uv` installed. If you don't, you can install it using:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

To sync the dependencies and set up the virtual environment (`.venv`), run:
```bash
uv sync
```

### Database Migrations

Run database migrations to initialize the SQLite database:
```bash
uv run python manage.py migrate
```

### Running the Development Server

Start the local development server:
```bash
uv run python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000/`.

## Project Configuration

- `pyproject.toml`: Project dependencies and metadata.
- `.python-version`: Declares Python 3.12 target version.
- `core/settings.py`: Main Django settings, pre-configured with `python-dotenv`, CORS support (`django-cors-headers`), and Django REST Framework.
- `.env`: Environment variables for development.
- `.env.example`: Template for environment variables.

## Adding Packages

To add dependencies, use `uv`:
```bash
uv add <package_name>
```
