"""
As with any standard Python function, you can pass parameters to your flow 
function, which are then used elsewhere in your flow. Prefect flows and 
tasks include the ability to perform type conversion for the parameters 
passed to your flow function. 


"""

from prefect import task, flow

@task
def printer(obj):
    print(f"Received a {type(obj)} with value {obj}")

# note that we define the flow with type hints
@flow
def validation_flow(x: int, y: str):
    printer(x)
    printer(y)

# wrond input types
validation_flow(x="42", y=100)