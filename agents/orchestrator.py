from graph.state import SupportState

def route_ticket(state: SupportState) -> str:
    """Router function to decide which specialist agent should handle the ticket based on triage category."""
    
    category = state.get("category", "").lower()
    
    if "billing" in category:
        return "billing"
    elif "technical" in category or "tech" in category:
        return "technical"
    elif "complaint" in category:
        return "complaint"
    else:
        # Fallback to technical agent if category is unrecognized
        return "technical"
