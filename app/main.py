import os
from agno.agent import Agent

from agno.models.openai import OpenAILike
from agno.tools.duckduckgo import DuckDuckGoTools

from textwrap import dedent
from agno.agent import RunOutput
from agno.utils.pprint import pprint_run_response

agent_instruction = dedent(
    """\
        You are a Web Search Agent.
        Your task is to perform targeted web searches to find accurate and relevant information on specific topics and edge cases related to atmospheric data, climate research, and environmental science.
    \
    """
)

model_id=os.getenv("MODEL_NAME")
base_url=os.getenv("BASE_URL")
api_key=os.getenv("API_KEY")
debug_mode=True

search_agent = Agent(
        id="web-search-agent",
        name="Web Knowledge Searcher",
        model=OpenAILike(
            id=model_id, base_url=base_url, api_key=api_key
        ),
        # Instructions for the agent
        instructions=agent_instruction,
        tools=[DuckDuckGoTools()],
        markdown=True,
        debug_mode=debug_mode,
        # stream=True,
        role="Perform targeted searches on specific topics and edge cases",
    )



# response: RunOutput = search_agent.run("What new ARM field campaigns were conducted in 2025?")
# Print the response in markdown format
# pprint_run_response(response, markdown=True)
# search_agent.print_response("Who is the director of ARM Data Center?")
search_agent.cli_app(stream=True)