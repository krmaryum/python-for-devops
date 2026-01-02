"""
Application entry point.

Run the API locally:
    python main_entry_pt_execute.py

Or with uvicorn (recommended in production):
    uvicorn app.api_init_fastapi:app --host 0.0.0.0 --port 8000
"""

import uvicorn


def main() -> None:
    """Start the ASGI server."""
    uvicorn.run(
        "app.api_init_fastapi:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # convenient for local development
    )


if __name__ == "__main__":
    print("Starting DevOps Utilities API (FastAPI)...")
    main()
