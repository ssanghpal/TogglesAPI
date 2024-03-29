from pydantic import BaseModel
from typing import Optional

class ToggleDisplay(BaseModel):
    toggle_id:int
    description:str
    environment_level:str
    status:str
    created_by:str
    created_at:str
    last_modified_at:str
    notes:Optional[str]=None

class ToggleCreateDisplay(BaseModel):
    toggle_id:int
    toggle_desc:str
    environment_level:str
    toggle_status:str
    created_by:str
    #created_at:str
    notes:Optional[str]=None

class ToggleUpdateDisplay(BaseModel):
    toggle_status:str
    notes:Optional[str]=None