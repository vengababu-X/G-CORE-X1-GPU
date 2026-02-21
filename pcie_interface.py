# ========================================================
# G-CORE X1: PCIe GEN 5.0 HOST INTERFACE (HIF)
# FEATURE: x16 Link Negotiation & TLP Packet Handling
# PURPOSE: High-Speed CPU-to-GPU Communication
# ========================================================

import os
import time
import random

class PCIeController:
    def __init__(self):
        self.link_speed = "32 GT/s (Gen 5)"
        self.lanes = 16
        self.mtu = 4096 # Payload size

    def negotiate_link(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[96m" + "⇔"*30)
        print(" G-CORE X1: PCIe GEN 5.0 HOST INTERFACE")
        print("⇔"*30 + "\033[0m")
        
        print("[LINK] Initializing Link Training (L0 State)...")
        time.sleep(0.5)
        
        stages = ["Detect", "Polling", "Configuration", "Recovery", "L0 (Active)"]
        for stage in stages:
            print(f"  > PCIe State: {stage:<15} [WAIT]", end="\r")
            time.sleep(0.3)
            print(f"  > PCIe State: {stage:<15} [\033[92mDONE\033[0m]")

        print(f"\n[INFO] Link Established: PCIe x{self.lanes} @ {self.link_speed}")
        print("-" * 60)

    def data_burst(self):
        print("\033[93m[HOST->DEVICE] Streaming Vertex Data (TLP Packets)...\033[0m")
        
        total_transfer = 0
        for i in range(10):
            packet_size = random.randint(128, 512)
            total_transfer += packet_size
            
            # Visualizing Transaction Layer Packets (TLP)
            progress = "■" * (i + 1) + "□" * (9 - i)
            print(f"  TLP_SEQ_{i:03d} | Size: {packet_size}B | Buffer: [{progress}]", end="\r")
            time.sleep(0.15)
        
        print(f"\n\n\033[92m[SUCCESS] Transfer Complete: {total_transfer} MB loaded to VRAM.")
        print(f"[STATUS] Latency: 12ns | Error Rate: 0.000001%\033[0m")
        print("-" * 60)

if __name__ == "__main__":
    pcie = PCIeController()
    pcie.negotiate_link()
    pcie.data_burst()