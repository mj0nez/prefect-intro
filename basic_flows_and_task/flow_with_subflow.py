"""
Not only can you call task functions within a flow, but you can also call 
other flow functions! Child flows are called subflows and allow you to 
efficiently manage, track, and version common multi-task logic. See the Composing
flows section of the Flows documentation for details.

Whenever we run main_flow as above, a new run will be generated for common_flow 
as well. Not only is this run tracked as a subflow run of main_flow, but you 
can also inspect it independently in the UI!

https://docs.prefect.io/tutorials/flow-task/

"""

from prefect import flow

@flow
def common_flow(config: dict):
    print("I am a subgraph that shows up in lots of places!")
    intermediate_result = 42
    return intermediate_result

@flow
def main_flow():
    # do some things
    # then call another flow function
    data = common_flow(config={})
    # do more things

main_flow()
