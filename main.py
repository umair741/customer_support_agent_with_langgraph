# Agent tests
from graph.state import SupportState
from agents.triage import triage_agent

state = SupportState(
    customer_query="I was charged twice for my subscription",
    ticket_id="TKT-001",
    category="", 
    priority="", 
    triage_reason="",
    agent_notes=[], 
    suggested_resolution="", 
    final_response=""
)

result = triage_agent(state)
print(result)