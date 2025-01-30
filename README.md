# SDN-Based Disaster Recovery System 🚀

## Overview
This project demonstrates the implementation of a **Software-Defined Networking (SDN) Disaster Recovery System**. It focuses on **automated failover, real-time monitoring**, and **traffic rerouting** to ensure network reliability during outages or disasters.

## Key Features
- **Centralized Network Control**: Utilizes OpenDaylight as the SDN controller.
- **Automated Failover**: Dynamically reroutes traffic during link or device failures using OpenFlow rules.
- **Real-Time Monitoring**: Python-based scripts monitor network performance and generate alerts for potential disruptions.
- **Disaster Recovery Testing**: Simulates various failure scenarios to validate system resilience.

---

## Project Structure
- **`/docs`**: Documentation and architecture diagrams.
- **`/scripts`**: Python scripts for automation, monitoring, and failover.
- **`/configs`**: Configuration files for Mininet, OpenDaylight, and network topology.
- **`/results`**: Logs, reports, and analysis from disaster recovery simulations.
- **`/examples`**: Sample topologies and output visualizations.

---

## Technologies Used
- **SDN Controller**: [OpenDaylight](https://www.opendaylight.org/)
- **Network Emulator**: [Mininet](http://mininet.org/)
- **Programming Languages**: Python (for automation and monitoring)
- **Protocols**: OpenFlow for traffic management
- **Monitoring Tools**: Wireshark, custom Python scripts

---

## Setup Instructions
### 1. Prerequisites
- Install **Mininet**: `sudo apt-get install mininet`
- Install **OpenDaylight**: Follow instructions [here](https://docs.opendaylight.org/)
- Install required Python libraries:  
  ```bash
  pip install requests json argparse

### 2. Clone the Repository
    ```bash
    git clone https://github.com/your-username/SDN-Disaster-Recovery.git
    cd SDN-Disaster-Recovery

### 3.Run Mininet Topology
    ```bash
    sudo python configs/mininet_topology.py
### 4. Start OpenDaylight Controller
Start OpenDaylight:
     ```bash
     ./karaf
Load configuration: configs/opendaylight_config.json
### 5. Execute Failover Automation
    ```bash
     python scripts/failover_automation.py
Example Output

Automated Failover:
Traffic Monitoring Logs:
[INFO] Link Down Detected: Rerouting traffic...
[INFO] Failover Complete: Recovery Time = 8.5 second

### Results
Recovery time during simulated disasters: <10 seconds
System logs and performance metrics: Available in the results/ folder.

### Contribution
Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open a discussion first.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
