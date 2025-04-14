from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Initialize FastAPI app
app = FastAPI()

# Configure templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/boards", response_class=HTMLResponse)
async def boards(request: Request):
    return templates.TemplateResponse("boards.html", {"request": request})

@app.get("/board/{board_id}", response_class=HTMLResponse)
async def board_detail(request: Request, board_id: str):
    return templates.TemplateResponse("board.html", {"request": request, "board_id": board_id})

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)