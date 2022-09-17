"""
Caching refers to the ability of a task run to reflect a finished state without
actually running the code that defines the task. This allows you to efficiently 
reuse results of tasks that may be particularly "expensive" to run with every 
flow run. Moreover, Prefect makes it easy to share these states across flows 
and flow runs using the concept of a "cache key function".
"""

# Task results are cached in memory during a flow run and persisted to the 
# location specified by the PREFECT_LOCAL_STORAGE_PATH setting. 
# As a result, task caching between flow runs is currently limited to flow 
# runs with access to that local storage path.


# Task input hash
# One way to use cache_key_fn is to cache based on inputs by specifying task_input_hash. 
# If the input parameters to the task are the same, Prefect returns the cached results 
# rather than running the task again. 

import time
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

# Whenever each task run requested to enter a Running state, it provided its cache key
# computed from the cache_key_fn. The Prefect Orion orchestration engine identified 
# that there was a COMPLETED state associated with this key and instructed the run to 
# immediately enter the same state, including the same return values. 


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=1))
def hello_task(name_input):
    # Doing some work
    print(f"Saying hello {name_input}")
    return "hello " + name_input

@flow
def hello_flow(name_input):
    hello_task(name_input)


hello_flow("Marv")
hello_flow("Marv")
hello_flow("Dave")


"""
Cache key function

You can also define your own cache key function that returns a string cache 
key. As long as the cache key remains the same, the Prefect backend identifies 
that there is a COMPLETED state associated with this key and instructs the new 
run to immediately enter the same COMPLETED state, including the same return values.

In this example, you could provide different input, but the cache key remains the 
same if the sum of the inputs remains the same.
"""

def cache_key_from_sum(context, parameters):
    print(parameters)
    return sum(parameters["nums"])

@task(cache_key_fn=cache_key_from_sum, cache_expiration=timedelta(minutes=1))
def cached_task(nums):
    print('running an expensive operation')  
    time.sleep(3)
    return sum(nums)

@flow
def test_caching(nums):
    cached_task(nums)

test_caching([2,2])
test_caching([1,3])  # sum is the same, therefore cached task is used
test_caching([3,2])
