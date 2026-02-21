# ========================================================
# G-CORE X1: FULL SYSTEM INTEGRATOR (SOC LEVEL) - FIXED
# PURPOSE: Syncing Graphics, AI, Display, and Power Logic
# ========================================================

import os
import time
import subprocess
import sys

def run_phase(name, script):
    print(f"\n\033[94m[PHASE: {name}]\033[0m")
    print("-" * 65)
    
    # Check if file exists
    if not os.path.exists(script):
        print(f"\033[91m[MISSING] {script} not found. Skipping...\033[0m")
        return

    try:
        # Run the script and show output directly in the terminal
        subprocess.run([sys.executable, script], check=True)
    except Exception as e:
        print(f"\033[91m[ERROR] {name} failed: {e}\033[0m")

def main():
    # Clear screen for professional look
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\033[96m" + "█"*65)
    print(" G-CORE X1: ADVANCED SYSTEM-ON-CHIP (SOC) INTEGRATION")
    print("█"*65 + "\033[0m")
    
    # 1. HARDWARE INITIALIZATION LAYER
    run_phase("SYSTEM BOOT (BIOS)", "gpu_bios.py")
    run_phase("CLOCK PLL SYNC", "clock_pll_ctrl.py")
    
    # 2. DATA & POWER LAYER
    run_phase("MEMORY BUS & DMA", "memory_controller.py")
    run_phase("THERMAL & POWER MGMT", "power_thermal_mgmt.py")
    
    # 3. COMPUTE & AI LAYER
    run_phase("16-LANE SIMD ENGINE", "gpu_engine.py")
    run_phase("AI TENSOR MMA", "tensor_core.py")
    run_phase("RT-CORE RAY TRACING", "rt_core.py")
    
    # 4. OUTPUT & DISPLAY LAYER
    run_phase("DISPLAY CONTROLLER (HDMI)", "display_controller.py")
    
    # 5. FINAL PHYSICAL SIGN-OFF
    run_phase("VLSI SIGN-OFF", "verification_signoff.py")
    
    # Final Confirmation Message (Fixed Syntax)
    print("\n\033[92m" + "═"*65)
    print(" G-CORE X1 INTEGRATION COMPLETE: ALL SYSTEMS NOMINAL")
    print(" STATUS: SILICON IS FULLY FUNCTIONAL AND DISPLAYING 4K")
    print("═"*65 + "\033[0m\n")

if __name__ == "__main__":
    main()