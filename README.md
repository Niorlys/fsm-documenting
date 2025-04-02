# FSM with Interactive SVG Docs

This project shows how to document a Finite State Machine (FSM) using an interactive SVG diagram where each state is clickable and links to the relevant documentation.

## 🔧 How to generate the diagram

Make sure [Graphviz](https://graphviz.org/download/) is installed. Then run:

```bash
dot -Tsvg fsm.dot -o fsm.svg
