"""
Task runners are responsible for running Prefect tasks within a flow. 
Each flow has a task runner associated with it. Depending on the task 
runner you use, the tasks within your flow can run sequentially, 
concurrently, or in parallel. You can even configure task runners 
to use distributed execution infrastructure such as a Dask cluster.

The default task runner is the ConcurrentTaskRunner, 
which will run submitted tasks concurrently. If you don't specify 
a task runner, Prefect uses the ConcurrentTaskRunner.

*ConcurrentTaskRunner for non-blocking, concurrent execution of tasks.*

All Prefect task runners support asynchronous task execution.

https://docs.prefect.io/concepts/task-runners/
"""

# Here we want a sequential task execution
from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner

@task
def first_task(num):
    return num + num

@task
def second_task(num):
    return num * num

@flow(name="My Sequential Flow", 
      task_runner=SequentialTaskRunner(),
)
def my_flow(num):
    plusnum = first_task.submit(num)
    sqnum = second_task.submit(plusnum)
    print(f"add: {plusnum.result()}, square: {sqnum.result()}")

my_flow(5)



import time
from prefect import task, flow
from prefect.task_runners import SequentialTaskRunner

@task
def print_values(values):
    for value in values:
        time.sleep(0.5)
        print(value, end="\r")

@flow(task_runner=SequentialTaskRunner())
def my_flow():
    print_values.submit(["AAAA"] * 15)
    print_values.submit(["BBBB"] * 10)

if __name__ == "__main__":
    my_flow()
