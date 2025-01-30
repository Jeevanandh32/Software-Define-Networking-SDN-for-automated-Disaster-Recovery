import requests

CONTROLLER_IP = "127.0.0.1"
CONTROLLER_PORT = "8181"
USERNAME = "admin"
PASSWORD = "admin"

BASE_URL = f"http://{CONTROLLER_IP}:{CONTROLLER_PORT}/restconf"

def add_flow(node_id, table_id, flow_id, in_port, out_port):
    flow = {
        "flow": {
            "id": flow_id,
            "priority": "100",
            "match": {"in-port": in_port},
            "instructions": {
                "apply-actions": {"output-action": {"output-node-connector": out_port}}
            },
        }
    }
    url = f"{BASE_URL}/config/opendaylight-inventory:nodes/node/{node_id}/table/{table_id}/flow/{flow_id}"
    response = requests.put(url, json=flow, auth=(USERNAME, PASSWORD))
    if response.status_code == 200:
        print(f"[SUCCESS] Flow {flow_id} added to node {node_id}.")
    else:
        print(f"[ERROR] Failed to add flow {flow_id}.")

if __name__ == "__main__":
    add_flow("openflow:1", 0, "flow1", "1", "2")
