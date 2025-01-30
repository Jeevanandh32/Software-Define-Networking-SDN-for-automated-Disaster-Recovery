from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI

def create_topology():
    net = Mininet(controller=Controller, switch=OVSSwitch)
    print("[INFO] Creating network topology...")

    # Add controller
    c0 = net.addController("c0")

    # Add switches
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")

    # Add hosts
    h1 = net.addHost("h1")
    h2 = net.addHost("h2")

    # Add links
    net.addLink(h1, s1)
    net.addLink(s1, s2)
    net.addLink(s2, h2)

    # Start network
    net.start()
    print("[INFO] Network started. Use CLI to interact.")
    CLI(net)
    net.stop()

if __name__ == "__main__":
    create_topology()
