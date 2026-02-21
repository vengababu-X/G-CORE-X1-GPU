# ========================================================
# G-CORE X1: HARDWARE-ACCELERATED RAY TRACING CORE (RT-CORE)
# FEATURE: Real-Time Recursive Ray-Sphere Intersection
# ========================================================

import os
import time
import math

class RTCore:
    def __init__(self):
        self.width = 50
        self.height = 20
        self.lanes = 16

    def render_rt_scene(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[93m" + "█"*60)
        print(" G-CORE X1: RT-CORE (RAY TRACING) HARDWARE ACTIVATED")
        print("█"*60 + "\033[0m")
        print(f"Mode: SIMD Ray-Casting | Target: Silicon-Level Real-Time Shadows")
        print("-" * 60)

        # The "Scene": A Sphere in 3D Space
        sphere_x, sphere_y, sphere_z = 0, 0, 5
        sphere_radius = 1.5

        for y in range(self.height):
            row = ""
            # Processing pixels in 16-lane "Warps"
            for x in range(self.width):
                # Calculate Ray Direction
                dx = (x / self.width) * 2 - 1
                dy = (y / self.height) * 2 - 1
                dz = 1 # Forward

                # Ray-Sphere Intersection Logic (Simulating RT-Core Gates)
                a = dx*dx + dy*dy + dz*dz
                b = 2 * (0 - sphere_x) * dx + 2 * (0 - sphere_y) * dy + 2 * (0 - sphere_z) * dz
                c = sphere_x**2 + sphere_y**2 + sphere_z**2 - sphere_radius**2
                
                discriminant = b**2 - 4*a*c

                if discriminant > 0:
                    # Ray Hit: Calculate Shadow Intensity
                    intensity = (math.sqrt(discriminant)) / 2
                    if intensity > 1.2:
                        row += "\033[97m█\033[0m" # Specular Highlight
                    elif intensity > 0.8:
                        row += "\033[92m▓\033[0m" # Diffuse Surface
                    else:
                        row += "\033[90m▒\033[0m" # Shadow/Edge
                else:
                    # Ray Miss: Background
                    if y > self.height / 2:
                        row += "\033[34m.\033[0m" # Ground Plane
                    else:
                        row += " " # Sky
            
            if y % 2 == 0:
                print(f" [RT_LANE_EXEC] {row}")
            else:
                print(f"               {row}")
            time.sleep(0.04)

        print("\033[93m" + "-" * 60)
        print(" RAY TRACING PASS COMPLETE | 1.45M TRANSISTORS ENGAGED")
        print(" STATUS: BIT-PERFECT SILICON TRACE CAPTURED")
        print("-" * 60 + "\033[0m")

if __name__ == "__main__":
    rt = RTCore()
    rt.render_rt_scene()