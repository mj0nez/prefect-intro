"""
Flow retries use the same argument syntax as task retry configuration. 
Note that retries for failed flows will retry the flow, tasks within the 
flow, and any child flows, and those are potentially subject to any 
configured retries.
"""

from prefect import flow, task

# this tasks runs 3 times before the flow fails
@task(retries=2, retry_delay_seconds=60)
def failure():
    print('running')
    raise ValueError("bad code")

@flow
def test_retries():
    return failure()



test_retries()