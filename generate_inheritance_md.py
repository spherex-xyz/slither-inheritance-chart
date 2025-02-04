from slither.slither import Slither
import subprocess

# Replace this with the path to your Solidity protocol
target_path = "/path/to/protocol"


def generate_mermaid_diagram(target_path):
    # Creating a new graph, a set to track edges, and a set to track nodes
    mermaid_diagram = ["graph LR;"]
    edges = set()
    nodes = set()

    subprocess.check_call(["solc-select", "use", "--always-install", "0.8.15"])
    slither_protocol_object = Slither(target_path)

    for contract in slither_protocol_object.contracts:
        contract_name = contract.name
        base_contracts = [
            base_contract.name for base_contract in contract.immediate_inheritance
        ]

        # Add node with color based on abstract status
        if contract.is_abstract:
            mermaid_diagram.append(f"    {contract_name}[{contract_name}]")
        else:
            mermaid_diagram.append(
                f"    {contract_name}[{contract_name}]:::nonAbstract"
            )

        nodes.add(contract_name)

        for base_contract in base_contracts:
            edge = f"{contract_name} --> {base_contract}"
            if edge not in edges:
                edges.add(edge)
                mermaid_diagram.append(f"    {edge};")

    # Add styles to the diagram
    mermaid_diagram.append(
        """
    classDef nonAbstract fill:#f9f,stroke:#333,stroke-width:2px;
    """
    )

    return "\n".join(mermaid_diagram)


if __name__ == "__main__":
    mermaid_code = generate_mermaid_diagram(target_path)
    print(mermaid_code)
