"""
Simply decorating functions as flows and tasks lets you take advantage of the 
orchestration and visibility features enabled by the Prefect Orion 
orchestration engine. You can also configure additional options on your flows
and tasks, enabling Prefect to execute and track your workflows more effectively.
"""

# A flow name is a distinguished piece of metadata within Prefect. 
# The name that you give to a flow becomes the unifying identifier for all future 
# runs of that flow, regardless of version or task structure.

from prefect import flow

@flow(name="My Example Flow_",description="Hello World!")
def my_flow():
    print("Hello World!")
    my_flow_2()
    my_flow_3()
    # run tasks and subflows


# A flow description enables you to provide documentation right 
# alongside your flow object. You can also provide a specific 
# description string as a flow option.
@flow(name="My Example Flow with description", 
      description="An example flow for a tutorial.")
def my_flow_2():
    print("Flow with description")

# A flow version enables you to associate a given run of your 
# workflow with the version of code or configuration that was used.
# If you are using git to version control your code, you might use 
# the commit hash as the version. 
#
# You don't have to supply a version for your flow. By default, 
# Prefect makes a best effort to compute a stable hash of the .py 
# file in which the flow is defined to automatically detect when 
# your code changes. 
# 
# However, this computation is not always 
# possible and so, depending on your setup, you may see that your 
# flow has a version of None.
@flow(name="My Example Flow with doc str description",version="tutorial_02")
def my_flow_3():
    """This is the flows description as docstring."""
    print("Flow with doc str description")

if __name__ == "__main__":
    my_flow()

    print(my_flow.description)