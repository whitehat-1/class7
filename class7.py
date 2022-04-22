from fastapi import FastAPI,HTTPException,UploadFile,File,Form
from typing import Optional 


app = FastAPI()


@app.get("/items/")
async def items():
    return{ "message": "hello world"}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: Optional [UploadFile]= None):
    if file is None:
        raise HTTPException(status_code=400, detail="file is required")
  
    return {"filename": file.filename}