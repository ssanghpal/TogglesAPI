from fastapi import FastAPI,status,Response,HTTPException
from .import schemas
from .import models
from .database import engine, sessionlocal, get_db
from fastapi.params import Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
app=FastAPI()
 
models.Base.metadata.create_all(engine)

@app.post('/toggles',status_code=status.HTTP_201_CREATED,response_model=schemas.ToggleDisplay)
def add(request:schemas.ToggleCreateDisplay,db:Session=Depends(get_db)):
    current_time=datetime.now()
    new_toggle=models.Toggle(toggle_id=request.toggle_id,description=request.toggle_desc,environment_level=request.environment_level,status=request.toggle_status,created_by=request.created_by,created_at=current_time,last_modified_at=current_time,notes=request.notes)
    db.add(new_toggle)
    db.commit()
    db.refresh(new_toggle)
    return new_toggle  

@app.get('/toggles',response_model=list[schemas.ToggleDisplay])
def get_all_toggles( db:Session=Depends(get_db)):
    toggles=db.query(models.Toggle).all()
    return toggles

@app.get('/toggles/{id}',response_model=schemas.ToggleDisplay)
def get(id:int,response:Response, db:Session=Depends(get_db)):
    toggle=db.query(models.Toggle).filter(models.Toggle.toggle_id==id).first()
    if not toggle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="toggle with id not found")
    return toggle

@app.put('/toggles/{id:int}',response_model=schemas.ToggleDisplay)
def update(id,request:schemas.ToggleUpdateDisplay,db:Session=Depends(get_db)):
    current_time=datetime.now()
    toggle=db.query(models.Toggle).filter(models.Toggle.toggle_id==id).first()
    if not toggle:
        raise HTTPException(status_code=404, detail="Toggle not found")
    else:
        toggle.status=request.toggle_status
        toggle.notes=request.notes
        toggle.last_modified_at=current_time
        db.commit()
        db.refresh(toggle)
        return toggle
    