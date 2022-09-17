"""
You can see that Prefect coerced the provided inputs into the types specified 
on your flow function!

While the above example is basic, this can be extended in powerful ways. 
In particular, Prefect attempts to coerce any pydantic model type hint 
into the correct form automatically:
https://pydantic-docs.helpmanual.io/usage/models/
"""

from prefect import flow, task
from pydantic import BaseModel

class Model(BaseModel):
    a: int
    b: float
    c: str

@task
def printer(obj):
    print(f"Received a {type(obj)} with value {obj}")

@flow
def model_validator(model: Model):
    printer(model)

model_validator({"a": 42, "b": 0, "c": 55})
