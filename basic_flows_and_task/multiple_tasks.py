"""
Notice in the above example that all of our Python logic is encapsulated within
task functions. While there are many benefits to using Prefect in this way, it 
is not a strict requirement. Using tasks enables Prefect to automatically identify 
the execution graph of your workflow and provides observability of task execution 
in the Prefect UI.

https://docs.prefect.io/tutorials/flow-task/
"""

import requests
from prefect import flow, task



@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@task
def parse_fact(response):
    fact = response["fact"]
    print(fact)
    return fact

@flow
def api_flow(url):
    fact_json = call_api(url)
    fact_text = parse_fact(fact_json)
    return fact_text

api_flow("https://catfact.ninja/fact")
