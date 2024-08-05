from slither.slither import Slither
import subprocess

# Replace this with the path to your Solidity protocol
target_path = "/path/to/your/protocol"


def generate_mermaid_diagram(target_path):
    # Creating a new graph and a set to track edges
    mermaid_diagram = ["graph TD;"]
    edges = set()

    subprocess.check_call(["solc-select", "use", "--always-install", "0.8.15"])
    slither_protocol_object = Slither(target_path)

    for contract in slither_protocol_object.contracts:
        contract_name = contract.name
        base_contracts = [
            base_contract.name for base_contract in contract.immediate_inheritance
        ]

        for base_contract in base_contracts:
            edge = f"{contract_name} --> {base_contract}"
            if edge not in edges:
                edges.add(edge)
                mermaid_diagram.append(f"    {edge};")

    return "\n".join(mermaid_diagram)


if __name__ == "__main__":
    mermaid_code = generate_mermaid_diagram(target_path)
    print(mermaid_code)
