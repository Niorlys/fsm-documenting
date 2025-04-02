import json
from sample_fsm import Matter

# Add basic state docstrings here manually (can also be structured differently)
state_docs = {
    "solid": "In the solid state, matter has a fixed shape and volume. Particles are tightly packed and vibrate in place.",
    "liquid": "In the liquid state, matter has a definite volume but takes the shape of its container.",
    "gas": "In the gas state, matter has no fixed shape or volume. Particles move freely."
}

# Collect transition method docstrings
transition_docs = {}
for method in ['melt', 'freeze', 'evaporate', 'condense']:
    doc = getattr(Matter, method).__doc__
    transition_docs[method] = doc.strip() if doc else ""

# Dump to JSON
docs = {
    "states": state_docs,
    "transitions": transition_docs
}

with open("fsm_docs.json", "w") as f:
    json.dump(docs, f, indent=2)

print("fsm_docs.json generated successfully.")
