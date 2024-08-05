# Mermaid Diagram Generator for Solidity Contracts

This project provides a Python script to generate a Mermaid.js diagram representing the inheritance relationships between Solidity contracts using Slither.

## Prerequisites

Before running the script, ensure you have the python installed:

- [Python](https://www.python.org/downloads/) (>= 3.6)

## Installation

1. **Clone this repository** (if applicable) or download the `generate_mermaid_diagram.py` script.

2. **Install required Python packages**:

   ```bash
   pip install slither-analyzer
   pip install solc-select
   ```

3. **Change the target_path** Make sure the target_path variable holds the path to your protocol.
   
4. **Run script**
   
   ```bash
   python generate_inheritance_md.py
   ```
