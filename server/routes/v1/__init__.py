from fastapi import FastAPI

from middlewares.exceptions import catch_exceptions_middleware
from routes.v1.projects import project_router

v1 = FastAPI()
v1.middleware('http')(catch_exceptions_middleware)

v1.include_router(project_router)
