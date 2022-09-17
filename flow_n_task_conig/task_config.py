"""
Tasks also accept tags as an option. Tags are runtime metadata used by the 
Prefect Orion orchestration engine that enable features like filtering 
display of task runs and configuring task concurrency limits.

You specify the tags on a task as a list of tag strings.
"""

from prefect import flow, task

@task(name="MyTask_361", 
      description="An example task for a tutorial.",
      tags=["tutorial","tag-test"])
def my_task_with_tags():
    print("some task....")

@flow
def my_flow_for_a_task_with_tags():
    my_task_with_tags()


my_flow_for_a_task_with_tags()