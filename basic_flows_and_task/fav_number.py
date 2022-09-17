"""
By adding the @flow decorator to a function, function calls will create a 
flow run — the Prefect Orion orchestration engine manages flow and task 
state, including inspecting their progress, regardless of where your flow code runs.
"""
from prefect import flow


@flow
def my_favorite_function():
    print("What is your favorite number?")
    return 42

print(my_favorite_function())



