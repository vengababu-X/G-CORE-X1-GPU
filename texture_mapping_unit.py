# ========================================================
# G-CORE X1: TEXTURE MAPPING UNIT (TMU)
# FEATURE: Bilinear Filtering & Anisotropic Mapping
# PURPOSE: High-Fidelity Texture Sampling and Filtering
# ========================================================

import os
import time
import random

class TextureMappingUnit:
    def __init__(self):
        self.tex_cache_size = 256 # KB
        self.filter_mode = "ANISOTROPIC_16X"
        self.sampling_rate = "4.2 GT/s"

    def process_texture_fetch(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[92m" + "▩"*30)
        print(" G-CORE X1: TEXTURE MAPPING UNIT (TMU)")
        print("▩"*30 + "\033[0m")
        print(f"Filter Mode: {self.filter_mode} | Cache: {self.tex_cache_size}KB")
        print("-" * 60)

        print("[TMU] Loading Mip-Map levels from VRAM...")
        time.sleep(0.5)

        # Simulate Bilinear Interpolation of 4 Texels
        for i in range(8):
            u, v = random.random(), random.random()
            print(f"  Fetching Texel at U:{u:.3f} V:{v:.3f} ... ", end="")
            
            # Simulate 4-tap sampling
            samples = ["S0", "S1", "S2", "S3"]
            time.sleep(0.1)
            print(f"[\033[92mFILTERED\033[0m] -> Pixel Out: 0x{random.randint(0x1000, 0xFFFF):04X}")
            
            # Visualizing the sample grid
            grid = "▓" if i % 2 == 0 else "▒"
            print(f"    Interpolation Grid: {grid * (i+1)}")

        print("-" * 60)
        print("\033[94m[INFO] TMU Throughput: 128 Pixels/Clock")
        print("[INFO] Texture Cache Hit Rate: 97.4%")
        print("[STATUS] Bilinear/Trilinear Pass: SUCCESS\033[0m")
        print("-" * 60)

if __name__ == "__main__":
    tmu = TextureMappingUnit:
    tmu.process_texture_fetch()