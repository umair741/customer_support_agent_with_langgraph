from graph.builder import support_graph
from graph.state import SupportState

def run_support_agent(query: str, ticket_id: str):
    print("\n" + "="*50)
    print(f"📥 NEW TICKET: {ticket_id}")
    print(f"💬 Customer Query: '{query}'")
    print("="*50)
    
    # 1. Initialize State
    initial_state = SupportState(
        customer_query=query,
        ticket_id=ticket_id,
        category="", 
        priority="", 
        triage_reason="",
        agent_notes=[], 
        suggested_resolution="", 
        final_response=""
    )
    
    # 2. Invoke the compiled LangGraph!
    print("🤖 Processing via LangGraph multi-agent system...")
    final_state = support_graph.invoke(initial_state)
    
    # 3. Print Results
    print("\n📋 Triaged Info:")
    print(f"   - Category: {final_state.get('category').upper()}")
    print(f"   - Priority: {final_state.get('priority').upper()}")
    print(f"   - Reason:   {final_state.get('triage_reason')}")
    
    print("\n📝 Specialist Notes:")
    for note in final_state.get("agent_notes", []):
        print(f"   • {note}")
    print(f"   - Suggested Resolution: {final_state.get('suggested_resolution')}")
    
    print("\n✉️ FINAL RESPONSE TO CUSTOMER:")
    print("-" * 50)
    print(final_state.get("final_response"))
    print("-" * 50)

if __name__ == "__main__":
    # Test 1: Billing Query
    run_support_agent(
        query="I noticed an extra charge of $15 on my credit card this month that I did not authorize. Please refund it.",
        ticket_id="TKT-BILL-901"
    )
    
    # Test 2: Technical Query
    run_support_agent(
        query="The application crashes instantly on my iPhone 15 Pro Max as soon as I tap the login button. I already tried reinstalling.",
        ticket_id="TKT-TECH-404"
    )