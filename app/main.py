from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Chinese Redefiner")

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 设置模板
templates = Jinja2Templates(directory="app/templates")

# 引入路由
from app.routers import explain

# 注册路由
app.include_router(explain.router)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 