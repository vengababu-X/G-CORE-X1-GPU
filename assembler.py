# ========================================================
# G-CORE X1: G-ISA MICROCODE ASSEMBLER (V1.0)
# FEATURE: Mnemonic-to-Binary Translation
# PURPOSE: Writing Low-Level Kernels for the 16-Lane Core
# ========================================================

import os
import json

class GCoreAssembler:
    def __init__(self):
        # Hardware Opcode Mapping
        self.OPCODES = {
            "LOAD": "V_LOAD",
            "ADD":  "V_ADD",
            "MUL":  "V_MUL",
            "SYNC": "V_SYNC",
            "NOP":  "V_SYNC" # No Operation
        }

    def assemble(self, input_file):
        if not os.path.exists(input_file):
            print(f"Error: {input_file} not found.")
            return

        print(f"\033[95m[ASSEMBLER] Reading Source: {input_file}...\033[0m")
        binary_output = []
        
        with open(input_file, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            # Clean the line (remove comments and whitespace)
            clean_line = line.split("//")[0].strip()
            if not clean_line: continue

            parts = clean_line.split()
            mnemonic = parts[0].upper()
            
            if mnemonic in self.OPCODES:
                # Handle Hex or Decimal operands
                raw_val = parts[1] if len(parts) > 1 else "0x0"
                val = int(raw_val, 16) if "0x" in raw_val else int(raw_val)
                
                binary_output.append((self.OPCODES[mnemonic], val))
                print(f"  Line {i+1:02d}: {mnemonic:<5} {raw_val:<6} -> {self.OPCODES[mnemonic]}")
            else:
                print(f"\033[91m  Error Line {i+1}: Unknown Instruction '{mnemonic}'\033[0m")

        # Save as the GPU Firmware
        with open("gpu_firmware.json", "w") as f:
            json.dump(binary_output, f)
        
        print(f"\033[92m[SUCCESS] Assembly Complete. 'gpu_firmware.json' generated.\033[0m")

if __name__ == "__main__":
    asm = GCoreAssembler()
    asm.assemble("kernel.gasm")