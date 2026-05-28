from langgraph.graph import StateGraph, START, END
from graph.state import SupportState
from agents.triage import triage_agent
from agents.billing import billing_agent
from agents.technical import technical_agent
from agents.complaint import complaint_agent
from agents.responder import responder_agent
from agents.orchestrator import route_ticket

def create_support_graph():
    # 1. Initialize StateGraph with our SupportState TypedDict
    workflow = StateGraph(SupportState)
    
    # 2. Add all agents as Nodes in the graph
    workflow.add_node("triage", triage_agent)
    workflow.add_node("billing", billing_agent)
    workflow.add_node("technical", technical_agent)
    workflow.add_node("complaint", complaint_agent)
    workflow.add_node("responder", responder_agent)
    
    # 3. Define Entrypoint
    workflow.add_edge(START, "triage")
    
    # 4. Add the Orchestrator Router as a Conditional Edge
    workflow.add_conditional_edges(
        "triage",          # Source node
        route_ticket,      
        {                  
            "billing": "billing",
            "technical": "technical",
            "complaint": "complaint"
        }
    )
    
    # 5. Connect all specialists to the Responder node
    workflow.add_edge("billing", "responder")
    workflow.add_edge("technical", "responder")
    workflow.add_edge("complaint", "responder")
    
    # 6. Responder marks the End of the graph execution
    workflow.add_edge("responder", END)
    
    # 7. Compile the graph
    return workflow.compile()

# Instantiated graph to import easily elsewhere
support_graph = create_support_graph()

if __name__ == "__main__":
    print("\n🗺️ Generating LangGraph Flowchart...")
    try:
        # Using draw_mermaid_png() to render and write PNG bytes
        png_bytes = support_graph.get_graph().draw_mermaid_png()
        with open("graph_flowchart.png", "wb") as f:
            f.write(png_bytes)
        print("🎨 Graph flowchart successfully saved to 'graph_flowchart.png'!")
    except Exception as e:
        print(f"Could not generate PNG: {e}")
