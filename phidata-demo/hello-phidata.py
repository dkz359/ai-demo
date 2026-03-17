from phi.agent import Agent, RunResponse
from phi.model.deepseek import DeepSeekChat

"""
issue: openai.UnprocessableEntityError: Failed to deserialize the JSON body into the target type: messages[0].role: unknown variant `developer`, expected one of `system`, `user`, `assistant`, `tool` at line 1 column 32
fixed: https://github.com/phidatahq/phidata/pull/1763/commits/a4b5160f01e65026e1c66b004be1c9502ca47af4
"""


agent = Agent(
    model=DeepSeekChat(),
    markdown=True
)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
