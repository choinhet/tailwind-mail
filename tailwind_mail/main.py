from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="tailwind_mail/static"), name="static")

templates = Jinja2Templates(directory="tailwind_mail/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html.jinja", context={}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
