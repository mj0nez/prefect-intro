"""
Let's now add some tasks to a flow so that we can orchestrate and monitor at a 
more granular level.

A task is a function that represents a distinct piece of work executed within a
flow. You don't have to use tasks — you can include all of the logic of your 
workflow within the flow itself. However, encapsulating your business logic 
into smaller task units gives you more granular observability, control over how 
specific tasks are run (potentially taking advantage of parallel execution), and
the ability to reuse tasks across flows and subflows.
"""

import requests
from prefect import flow, task
@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@flow
def api_flow(url):
    fact_json = call_api(url)
    return fact_json

print(api_flow("https://catfact.ninja/fact"))
