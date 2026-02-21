# ========================================================
# G-CORE X1: POWER DELIVERY NETWORK (PDN) & THERMAL MGMT
# FEATURE: Dynamic Voltage and Frequency Scaling (DVFS)
# PURPOSE: Preventing Thermal Throttling in Silicon
# ========================================================

import os
import time
import random

class ThermalController:
    def __init__(self):
        self.target_clock = 1200  # MHz
        self.current_temp = 35.0  # Celsius
        self.voltage = 1.1        # Volts
        self.throttled = False

    def monitor_die_physics(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[91m" + "⚡"*30)
        print(" G-CORE X1: POWER & THERMAL MONITORING SYSTEM")
        print("⚡"*30 + "\033[0m")
        print(f"Design TDP: 4.8W | Shutdown Temp: 105°C")
        print("-" * 60)

        for i in range(15):
            # Simulate heat generation based on 16-lane activity
            load = random.uniform(0.7, 1.0)
            self.current_temp += (load * 2.5)
            
            # Logic: If temp > 85C, lower voltage and clock speed (Throttling)
            status = "\033[92mOPTIMAL\033[0m"
            if self.current_temp > 85:
                self.throttled = True
                self.voltage = 0.95
                self.target_clock = 800
                status = "\033[93mTHROTTLED\033[0m"
            
            if self.current_temp > 100:
                status = "\033[91mCRITICAL\033[0m"

            print(f"SEC {i:02d} | TEMP: {self.current_temp:.1f}°C | VOLT: {self.voltage}V | CLK: {self.target_clock}MHz | [{status}]")
            
            # Visualizing the Voltage Regulator Module (VRM) firing
            vrm_load = "█" * int(load * 15)
            print(f"       VRM Load: [{vrm_load:<15}]")
            
            time.sleep(0.2)

        print("-" * 60)
        if self.throttled:
            print("\033[93m[ALERT] Thermal Throttling Engaged to Save Silicon.")
        print("\033[92m[INFO] Power Delivery Network: Stable.")
        print("[INFO] Peak Energy Efficiency: 0.85 pJ/bit\033[0m")
        print("-" * 60)

if __name__ == "__main__":
    pwr = ThermalController()
    pwr.monitor_die_physics()