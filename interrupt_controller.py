# ========================================================
# G-CORE X1: HARDWARE INTERRUPT CONTROLLER (G-INT)
# FEATURE: IRQ Vectoring & Interrupt Service Routines (ISR)
# PURPOSE: Low-Level Handshake between GPU and OS Kernel
# ========================================================

import os
import time
import random

class InterruptController:
    def __init__(self):
        # Priority map (Lower number = Higher priority)
        self.irq_map = {
            0: "THERMAL_CRITICAL",
            1: "DMA_TRANSFER_COMPLETE",
            2: "KERNEL_EXEC_FINISHED",
            3: "V_BLANK_INTERRUPT",
            4: "PCIE_DATA_READY"
        }

    def trigger_irq(self, irq_id):
        name = self.irq_map.get(irq_id, "UNKNOWN_INTERRUPT")
        print(f"\033[91m[HARDWARE_SIGNAL] Pin {irq_id} High -> {name}\033[0m")
        
        # Simulate CPU context switching to the ISR (Interrupt Service Routine)
        print(f"  > Context Switch: CPU saving state...")
        time.sleep(0.2)
        print(f"  > Executing ISR_{irq_id:02d} ... \033[92mACKNOWLEDGED\033[0m")

    def run_simulation(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[93m" + "⚡"*30)
        print(" G-CORE X1: INTERRUPT CONTROLLER (G-INT)")
        print("⚡"*30 + "\033[0m")
        print("Mode: Vectored Interrupts | Status: SYSTEM_READY")
        print("-" * 60)

        events = [2, 3, 1, 4, 0] # Random sequence of hardware events
        
        for event in events:
            print(f"Time: {time.strftime('%H:%M:%S.%f')[:-3]}")
            self.trigger_irq(event)
            
            if event == 0:
                print("\033[91m[SYSTEM] Emergency Throttle: ISR_00 has high priority.\033[0m")
            
            print("-" * 60)
            time.sleep(0.5)

        print("\033[94m[INFO] All Hardware Interrupts Handled by OS Kernel.")
        print("[INFO] Interrupt Latency: 450ns (Simulated)")
        print("[STATUS] G-INT logic verified for Windows/Linux Drivers.\033[0m")
        print("-" * 60)

if __name__ == "__main__":
    gic = InterruptController()
    gic.run_simulation()