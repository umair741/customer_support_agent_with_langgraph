from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from config.settings import GOOGLE_API_KEY, MODEL_NAME, TEMPERATURE, RESPONDER_PROMPT
from graph.state import SupportState

def responder_agent(state: SupportState) -> dict:
    """Formatter agent to construct the final response to the customer."""
    
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        google_api_key=GOOGLE_API_KEY,
    )

    # Gather context from previous agents
    context = (
        f"Ticket ID: {state['ticket_id']}\n"
        f"Category: {state['category']}\n"
        f"Priority: {state['priority']}\n"
        f"Agent Notes: {', '.join(state['agent_notes'])}\n"
        f"Suggested Resolution: {state['suggested_resolution']}"
    )

    response = llm.invoke([
        SystemMessage(content=RESPONDER_PROMPT),
        HumanMessage(content=f"{context}\n\nOriginal Customer Query: {state['customer_query']}"),
    ])

    return {
        "final_response": response.content
    }
