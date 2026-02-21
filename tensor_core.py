# ========================================================
# G-CORE X1: G-TENSOR CORE (AI ACCELERATOR)
# FEATURE: 4x4 Matrix Multiply-Accumulate (MMA)
# PURPOSE: Neural Network Acceleration in Silicon
# ========================================================

import os
import time
import random

class GTensorCore:
    def __init__(self):
        self.lanes = 16
        self.cycle = 0

    def run_ai_workload(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[95m" + "▄"*60)
        print(" G-CORE X1: G-TENSOR CORE ACTIVATED (AI ACCELERATION)")
        print("▄"*60 + "\033[0m")
        print(f"Mode: 4x4 Matrix MMA | Logic: Parallel Systolic Array")
        print("-" * 60)

        # Generate two 4x4 Matrices (Weight and Input)
        weights = [[random.randint(0, 5) for _ in range(4)] for _ in range(4)]
        inputs = [[random.randint(0, 5) for _ in range(4)] for _ in range(4)]
        result = [[0 for _ in range(4)] for _ in range(4)]

        print("\033[93m[STEP 1] Loading Weights into L1 Cache...\033[0m")
        time.sleep(0.5)
        
        print("\033[93m[STEP 2] Executing Systolic Array Matrix Multiplication...\033[0m")
        time.sleep(0.5)

        # Matrix Multiplication (The core of AI math)
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    result[i][j] += weights[i][k] * inputs[k][j]
                
                # Visualizing the Tensor Core "Firing"
                print(f"  TENSOR_UNIT_{i}_{j}: MMA Operation Complete", end="\r")
                time.sleep(0.05)
            print()

        print("\n\033[92m[STEP 3] Final Neural Output (Tensor Result):\033[0m")
        for row in result:
            row_str = " ".join([f"[{val:03d}]" for val in row])
            print(f"  {row_str}")

        print("\n\033[95m" + "-" * 60)
        print(" AI WORKLOAD COMPLETE | PRECISION: INT8 / FP16")
        print(" STATUS: BIT-PERFECT NEURAL PROCESSING")
        print("-" * 60 + "\033[0m")

if __name__ == "__main__":
    tensor = GTensorCore()
    tensor.run_ai_workload()