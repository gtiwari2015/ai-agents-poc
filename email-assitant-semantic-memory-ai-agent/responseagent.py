from prompts import agent_system_prompt
from langgraph.prebuilt import create_react_agent
from prompts import prompt_instructions
from tools import write_email, schedule_meeting, check_calendar_availability
from profileSetup import profile

def create_prompt(state):
    return [
        {
            "role": "system", 
            "content": agent_system_prompt.format(
                instructions=prompt_instructions["agent_instructions"],
                **profile
                )
        }
    ] + state['messages']
print(agent_system_prompt)
tools=[write_email, schedule_meeting, check_calendar_availability]
response_agent = create_react_agent(
    "openai:gpt-4o",
    tools=tools,
    prompt=create_prompt,
)
response = response_agent.invoke(
    {"messages": [{
        "role": "user", 
        "content": "what is my availability for tuesday?"
    }]}
)
response["messages"][-1].pretty_print()