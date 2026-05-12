from typing import TypedDict  # ← yeh line missing thi

class SupportState(TypedDict):
    customer_query: str
    ticket_id: str
    category: str                 # billing | technical | complaint
    priority: str                 # low | medium | high | urgent
    triage_reason: str            # Why it was categorized this way
    agent_notes: list[str]        # Notes from the specialist
    suggested_resolution: str     # Specialist's proposed fix
    final_response: str           # Final formatted reply