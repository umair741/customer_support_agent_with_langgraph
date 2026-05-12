from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from config.settings import GOOGLE_API_KEY, MODEL_NAME, TEMPERATURE, TRIAGE_PROMPT
from graph.state import SupportState

class TriageOutput(BaseModel):
    category: str       
    priority: str       
    triage_reason: str  

def triage_agent(state: SupportState) -> dict:

    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        google_api_key=GOOGLE_API_KEY,
    ).with_structured_output(TriageOutput)  

    
    response = llm.invoke([
        SystemMessage(content=TRIAGE_PROMPT),
        HumanMessage(content=state["customer_query"]),
    ])

    
    return {"category": response.category,"priority": response.priority,"triage_reason": response.triage_reason,
    }