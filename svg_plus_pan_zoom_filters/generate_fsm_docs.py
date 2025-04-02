import json
from fsm_sample import DocumentWorkflow

# Step 1: define state docs manually
state_docs = {
    "draft": "Initial editable state of the document.",
    "review": "The document is under review by peers or supervisors.",
    "corrections": "Requested changes are being made to the document.",
    "approved": "The document has been approved and is awaiting signature.",
    "signed": "The document has been officially signed.",
    "published": "The signed document has been published.",
    "archived": "The document has been archived.",
    "reopened": "An archived document has been reopened for modification.",
    "rejected": "The document was rejected during review.",
    "deleted": "The document was deleted and is no longer accessible.",
    "retracted": "A published document was pulled back from public view."
}

# Step 2: list only your real transition method names
manual_transitions = [
    "submit", "request_changes", "resubmit", "approve", "sign",
    "publish", "archive", "reopen", "delete", "reject", "retract"
]

# Step 3: extract docstrings safely
transition_docs = {}
for method_name in manual_transitions:
    method = getattr(DocumentWorkflow, method_name, None)
    if method and method.__doc__:
        transition_docs[method_name] = method.__doc__.strip()
    else:
        transition_docs[method_name] = "No documentation available."

# Step 4: write to JSON
docs = {
    "states": state_docs,
    "transitions": transition_docs
}

with open("fsm_docs.json", "w") as f:
    json.dump(docs, f, indent=2)

print("✅ fsm_docs.json generated successfully.")
