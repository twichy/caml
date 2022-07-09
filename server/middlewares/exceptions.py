import traceback

from fastapi.requests import Request
from fastapi.responses import JSONResponse

from caml.errors import CamlConflictError, CamlError, CamlNotFoundError


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except CamlConflictError as e:
        traceback.print_exc()
        return JSONResponse(content={"error": str(e)}, status_code=409)
    except CamlNotFoundError as e:
        traceback.print_exc()
        return JSONResponse(content={"error": str(e)}, status_code=404)
    except CamlError as e:
        traceback.print_exc()
        return JSONResponse(content={"error": str(e)}, status_code=422)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"error": "An internal error has occurred"}, status_code=500)
