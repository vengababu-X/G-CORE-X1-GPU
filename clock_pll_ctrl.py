# ========================================================
# G-CORE X1: CLOCK DISTRIBUTION & PLL CONTROLLER
# FEATURE: Frequency Synthesis & Clock Gating
# PURPOSE: Generating 1.2GHz Logic Heartbeat from Ref Clock
# ========================================================

import os
import time
import random
import math

class ClockController:
    def __init__(self):
        self.ref_clock_mhz = 25.0
        self.target_mhz = 1200.0
        self.pll_locked = False
        self.jitter_ps = 0 # Picoseconds

    def synthesize_frequency(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[96m" + "〰"*30)
        print(" G-CORE X1: PLL & CLOCK DISTRIBUTION TREE")
        print("〰"*30 + "\033[0m")
        print(f"Ref Clock: {self.ref_clock_mhz}MHz | Target: {self.target_mhz}MHz")
        print("-" * 60)

        print("[PLL] Initiating Frequency Lock Loop...")
        time.sleep(0.5)

        # Simulate the PLL finding the correct multiplier
        multiplier = self.target_mhz / self.ref_clock_mhz
        current_freq = 0.0
        
        for i in range(1, 11):
            # Gradually converge on the target frequency
            current_freq = self.target_mhz * (i / 10.0)
            self.jitter_ps = random.uniform(2.0, 15.0)
            
            # Visualizing the sine-wave stabilization
            wave = " " * int(10 + 5 * math.sin(i)) + "⚡"
            print(f"  Step {i:02d}: {current_freq:>7.1f} MHz | Jitter: {self.jitter_ps:.2f}ps | {wave}")
            time.sleep(0.2)

        self.pll_locked = True
        print(f"\n\033[92m[SUCCESS] PLL LOCKED at {self.target_mhz} MHz (Mult: x{multiplier})\033[0m")
        print("-" * 60)

    def clock_gating_test(self):
        print("\033[93m[POWER] Testing Dynamic Clock Gating...\033[0m")
        time.sleep(0.5)
        
        # Simulate turning off clock to idle lanes to save power
        active_lanes = [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
        
        tree_viz = ""
        for lane in active_lanes:
            if lane == 1:
                tree_viz += "\033[92mON \033[0m"
            else:
                tree_viz += "\033[90mOFF\033[0m"
        
        print(f"  Clock Tree Status: {tree_viz}")
        print(f"  Efficiency Gain: +22% Power Saved via Gating.")
        print("-" * 60)

if __name__ == "__main__":
    clk = ClockController()
    clk.synthesize_frequency()
    clk.clock_gating_test()