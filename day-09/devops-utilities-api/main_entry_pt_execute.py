# Application Entry Point

from app.api_init_fastapi import app
import uvicorn

if __name__ == '__main__':
    print('ASGI (Asynchronous Server Gateway Interface) Web Server Running...')
    uvicorn.run(
        "app.api_init_fastapi:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

#"""
#app.api:app
#│   │     └── FastAPI instance (app/variable name)
#│   └──────── api_init_fastapi.py file
#└──────────── app folder (package)
#
#127.0.0.1 ---> localhost only, 0.0.0.0 ---> accessible from any network interface
#
#"""