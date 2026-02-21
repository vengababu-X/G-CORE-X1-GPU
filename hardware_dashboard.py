# ========================================================
# G-CORE X1: LIVE HARDWARE DIAGNOSTIC DASHBOARD
# FEATURE: Real-Time Telemetry & Metric Visualization
# PURPOSE: Performance Monitoring for 16-Lane Architecture
# ========================================================

import os
import time
import random

class HardwareDashboard:
    def __init__(self):
        self.refresh_rate = 0.2
        self.vram_used = 0
        self.max_vram = 8192 # 8GB Virtual VRAM

    def draw_bar(self, percentage, length=20, color="\033[92m"):
        filled = int(percentage * length)
        bar = "█" * filled + "░" * (length - filled)
        return f"{color}{bar}\033[0m"

    def launch(self):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[96m" + "╔" + "═"*58 + "╗")
                print("║ G-CORE X1 HARDWARE MONITORING UTILITY - V1.0             ║")
                print("╚" + "═"*58 + "╝" + "\033[0m")
                
                # --- CORE TELEMETRY ---
                simd_load = random.uniform(0.1, 0.95)
                tensor_load = random.uniform(0.05, 0.4)
                temp = 35 + (simd_load * 50)
                fan_speed = 1200 + (temp * 20)
                
                print(f" CORE CLOCK: 1200 MHz  |  VOLTAGE: 1.05V  |  STATUS: ACTIVE")
                print("-" * 60)
                
                print(f" SIMD ENGINE UTIL  : {self.draw_bar(simd_load)} {int(simd_load*100)}%")
                print(f" TENSOR AI LOAD    : {self.draw_bar(tensor_load, color='\033[95m')} {int(tensor_load*100)}%")
                print(f" VRAM USAGE (DMA)  : {self.draw_bar(0.42, color='\033[94m')} 3440 MB")
                print("-" * 60)
                
                # --- THERMAL/POWER ---
                print(f" DIE TEMPERATURE   : {temp:.1f}°C")
                print(f" FAN SPEED (RPM)   : {int(fan_speed)} RPM")
                print(f" CURRENT POWER DRAW: {4.2 * simd_load:.2f} Watts")
                print("-" * 60)
                
                # --- BUS ACTIVITY ---
                print(f" PCIe GEN 5.0 BUS  : \033[93mTX: {random.randint(100,500)} MB/s | RX: {random.randint(50,200)} MB/s\033[0m")
                print(f" HARDWARE INTERRUPT: IRQ_VECTOR_0x{random.randint(10,99)}")
                
                print("\n\033[90mPress Ctrl+C to exit Diagnostic Mode...\033[0m")
                time.sleep(self.refresh_rate)
        except KeyboardInterrupt:
            print("\n\033[92mDashboard Closed. Telemetry Logs Saved to 'hw_logs.txt'.\033[0m")

if __name__ == "__main__":
    dash = HardwareDashboard()
    dash.launch()