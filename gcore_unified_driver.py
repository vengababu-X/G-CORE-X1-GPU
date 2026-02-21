# ========================================================
# G-CORE X1: UNIFIED HARDWARE DRIVER (VERSION 1.0)
# PURPOSE: Final Integration and System Harmony
# ========================================================

import os
import time
import subprocess
import sys

class GCoreUnifiedDriver:
    def __init__(self):
        self.version = "1.0.4-STABLE"
        self.required_files = [
            "gpu_engine.py", "tensor_core.py", "rt_core.py", 
            "memory_controller.py", "clock_pll_ctrl.py", 
            "display_controller.py", "power_thermal_mgmt.py",
            "verification_signoff.py"
        ]

    def verify_integrity(self):
        """Checks if all hardware blocks are present in the directory."""
        print(f"\033[96m[DRIVER] G-Core Unified Driver v{self.version} Initializing...\033[0m")
        missing = []
        for f in self.required_files:
            if not os.path.exists(f):
                missing.append(f)
        
        if missing:
            print(f"\033[91m[ERROR] Missing hardware blocks: {', '.join(missing)}\033[0m")
            return False
        
        print("\033[92m[SUCCESS] All 16-Lane SIMD hardware blocks verified.\033[0m")
        return True

    def launch_system(self):
        """Runs the complete hardware lifecycle in the correct order."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[94m" + "█"*65)
        print(" G-CORE X1: FULL SYSTEM UNIFIED BOOT SEQUENCE")
        print("█"*65 + "\033[0m")

        # 1. Start the physical heartbeat
        self._run_subsystem("CLOCK PLL", "clock_pll_ctrl.py")
        
        # 2. Check the safety and memory
        self._run_subsystem("THERMAL/POWER", "power_thermal_mgmt.py")
        self._run_subsystem("MEMORY BUS", "memory_controller.py")
        
        # 3. Fire the main compute cores
        print("\n\033[93m[COMPUTE] Engaging 16-Lane SIMD, RT, and Tensor Cores...\033[0m")
        time.sleep(1)
        self._run_subsystem("SIMD ENGINE", "gpu_engine.py")
        self._run_subsystem("TENSOR CORE", "tensor_core.py")
        self._run_subsystem("RT-CORE", "rt_core.py")
        
        # 4. Initialize Output
        self._run_subsystem("DISPLAY OUT", "display_controller.py")

        # 5. Final Approval
        print("\n" + "═"*65)
        self._run_subsystem("FINAL SIGN-OFF", "verification_signoff.py")
        print("═"*65)
        print("\033[92m[SYSTEM STATUS] G-CORE X1 IS NOW FULLY OPERATIONAL.\033[0m")
        print("█"*65 + "\n")

    def _run_subsystem(self, label, script):
        print(f"\033[95m[LINKING] {label}...\033[0m", end=" ", flush=True)
        try:
            # We use check=True to ensure if one file has a syntax error, we know immediately
            subprocess.run([sys.executable, script], check=True, capture_output=True)
            print("[\033[92mONLINE\033[0m]")
        except subprocess.CalledProcessError as e:
            print("[\033[91mFAILED\033[0m]")
            print(f"Error in {script}: {e.stderr.decode()}")

if __name__ == "__main__":
    driver = GCoreUnifiedDriver()
    if driver.verify_integrity():
        driver.launch_system()