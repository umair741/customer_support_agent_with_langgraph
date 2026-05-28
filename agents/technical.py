from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from config.settings import GOOGLE_API_KEY, MODEL_NAME, TEMPERATURE, TECHNICAL_PROMPT
from graph.state import SupportState

class TechnicalOutput(BaseModel):
    agent_notes: list[str] = Field(description="Internal notes about the technical issue, bug, or crash")
    suggested_resolution: str = Field(description="The proposed troubleshooting steps or fix for the customer")

def technical_agent(state: SupportState) -> dict:
    """Specialist agent to handle technical support queries, bugs, and issues."""
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        google_api_key=GOOGLE_API_KEY,
    ).with_structured_output(TechnicalOutput)

    context = f"Ticket ID: {state['ticket_id']}\nPriority: {state['priority']}\nTriage Reason: {state['triage_reason']}"
    
    response = llm.invoke([
        SystemMessage(content=TECHNICAL_PROMPT),
        HumanMessage(content=f"{context}\n\nCustomer Query: {state['customer_query']}"),
    ])

    return {
        "agent_notes": response.agent_notes,
        "suggested_resolution": response.suggested_resolution
    }
