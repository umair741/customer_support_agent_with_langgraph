from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from config.settings import GOOGLE_API_KEY, MODEL_NAME, TEMPERATURE, BILLING_PROMPT
from graph.state import SupportState

class BillingOutput(BaseModel):
    agent_notes: list[str] = Field(description="Internal notes about the billing issue")
    suggested_resolution: str = Field(description="The proposed fix or next steps for the customer")

def billing_agent(state: SupportState) -> dict:
   
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        google_api_key=GOOGLE_API_KEY,
    
    ).with_structured_output(BillingOutput)

    
    context = f"Ticket ID: {state['ticket_id']}\nPriority: {state['priority']}\nTriage Reason: {state['triage_reason']}"
    
    response = llm.invoke([
        SystemMessage(content=BILLING_PROMPT),
        HumanMessage(content=f"{context}\n\nCustomer Query: {state['customer_query']}"),
    ])

    return {
        "agent_notes": response.agent_notes,
        "suggested_resolution": response.suggested_resolution
    }
