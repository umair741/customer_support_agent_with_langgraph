# test_billing.py banao ya directly main.py mein likho

from agents.triage import triage_agent
from agents.billing import billing_agent

# Fake state banao
test_state = {
    "ticket_id": "TICKET-001",
    "customer_query": "Mujhe November ka invoice nahi mila",
    "priority": "high",
    "triage_reason": "Customer billing issue report kar raha hai",
    "category": "billing"
}

# Billing agent run karo
result = billing_agent(test_state)

print("Agent Notes:", result["agent_notes"])
print("Resolution:", result["suggested_resolution"])