import requests
import time

# OpenDaylight controller details
CONTROLLER_IP = "127.0.0.1"
CONTROLLER_PORT = "8181"
USERNAME = "admin"
PASSWORD = "admin"

# REST API URL for OpenFlow
BASE_URL = f"http://{CONTROLLER_IP}:{CONTROLLER_PORT}/restconf"

def monitor_links():
    print("[INFO] Monitoring network links...")
    while True:
        response = requests.get(f"{BASE_URL}/operational/network-topology:network-topology", auth=(USERNAME, PASSWORD))
        if response.status_code == 200:
            topology = response.json()
            for link in topology.get("network-topology", {}).get("topology", [])[0].get("link", []):
                if link["link-state"] == "DOWN":
                    print(f"[ALERT] Link down detected: {link['link-id']}")
                    trigger_failover(link["source"]["node"], link["destination"]["node"])
        time.sleep(5)

def trigger_failover(src_node, dest_node):
    print(f"[INFO] Rerouting traffic from {src_node} to {dest_node}...")
    # Add OpenFlow failover rules
    data = {
        "flow": {
            "id": "failover1",
            "priority": "100",
            "match": {"in-port": "1"},
            "instructions": {
                "apply-actions": {"output-action": {"output-node-connector": "2"}}
            },
        }
    }
    url = f"{BASE_URL}/config/opendaylight-inventory:nodes/node/{src_node}/table/0/flow/1"
    response = requests.put(url, json=data, auth=(USERNAME, PASSWORD))
    if response.status_code == 200:
        print("[SUCCESS] Traffic rerouted successfully.")
    else:
        print("[ERROR] Failed to apply failover rules.")

if __name__ == "__main__":
    monitor_links()
