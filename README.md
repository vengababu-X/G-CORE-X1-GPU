<div align="center">

# 🚀 G-CORE-X1 GPU  
### 🧠 A Multi-Core SIMD GPU — Built from Scratch in RTL

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=00F7FF&center=true&vCenter=true&width=750&lines=Multi-Core+SIMD+GPU;RTL+Implemented+%7C+Simulated;Parallel+Compute+Architecture;Instruction-Driven+Execution;Verified+Using+Waveforms" />

</div>

---

## 🟢 Project Status

```diff
+ RTL DESIGN COMPLETE
+ SIMD EXECUTION VERIFIED
+ MULTI-CORE GPU IMPLEMENTED
+ LOAD / STORE MEMORY WORKING
+ SIMULATION WAVEFORMS GENERATED


---
```
📌 What Is G-CORE-X1?

G-CORE-X1 is a real GPU compute architecture, implemented at Register Transfer Level (RTL) using Verilog.

This project focuses on the core execution engine of a GPU, not graphics output.

✔ Parallel execution
✔ SIMD / Vector processing
✔ Multi-core architecture
✔ Instruction-based execution
✔ Verified via simulation

❌ Not a graphics card
❌ No HDMI / display output
❌ No fake performance charts
```

---

⚡ Animated Architecture Overview

┌──────────────────────────── GPU CORE ────────────────────────────┐
│                                                                   │
│   🧠 Instruction Memory  ──▶  Program Counter  ──▶ Decode Logic   │
│                                                                   │
│   ┌──────────────────┐              ┌──────────────────┐         │
│   │   COMPUTE UNIT 0 │              │   COMPUTE UNIT 1 │         │
│   │──────────────────│              │──────────────────│         │
│   │ SIMD ALU (Vector)│              │ SIMD ALU (Vector)│         │
│   │ Reg File         │              │ Reg File         │         │
│   │ Data Memory      │              │ Data Memory      │         │
│   └──────────────────┘              └──────────────────┘         │
│                                                                   │
│            🔗 Global Interconnect + ⏱ Clock Network               │
└───────────────────────────────────────────────────────────────────┘


---
```
🧩 GPU Design Layers (Animated Explanation)

🔹 Layer 0 — SIMD ALU

Multi-lane vector ALU

ADD / MUL operations

Executes same instruction on multiple data elements


🔹 Layer 1 — Vector Register File

Multiple vector registers

Parallel read/write

Feeds SIMD ALU


🔹 Layer 2 — Instruction Fetch

Program Counter (PC)

Instruction Memory (IMEM)

Autonomous execution (no testbench control)


🔹 Layer 3 — Load / Store Memory

Local data memory

LOAD and STORE instructions

Memory-based computation support


🔹 Layer 4 — Multi-Core GPU

Two compute units instantiated

Identical execution units

Parallel execution under shared control



---
``
🧪 Simulation & Verification

✔ RTL simulation performed
✔ Waveforms generated (.vcd)
✔ Verified on EDA Playground
✔ EPWave used for signal analysis

✔ Verified Behavior

+ Program Counter increments correctly
+ Instructions fetched from IMEM
+ SIMD ALU executes vector operations
+ Register file write-back works
+ Load / Store memory verified
+ Multiple cores execute in parallel

📈 Waveforms are the simulation graphs
This is how real hardware is verified.

```
---

📂 Repository Structure

G-CORE-X1-GPU/
│
├── rtl/                # Verilog RTL modules
│   ├── simd_alu.v
│   ├── vector_regfile.v
│   ├── data_memory.v
│   ├── compute_unit.v
│   └── multi_core_gpu.v
│
├── testbench/          # Simulation testbenches
│   └── tb_multi_core.sv
│
├── simulations/        # Waveform outputs
│   └── *.vcd
│
├── docs/               # Architecture & diagrams
│
└── README.md           # This file


---
```
🧠 Circuit-Level View (Conceptual)

Instruction Memory feeds control logic

Control logic drives compute units

Each compute unit contains:

SIMD ALU

Vector Register File

Local Data Memory



This is a block-level circuit schematic, standard for GPU architectures.


---

🏗 Physical Layout (Conceptual)

Floorplan-level layout

Compute units tiled side-by-side

Shared instruction memory

Global interconnect & clock network


📌 This represents physical organization, not fabrication.


---

❓ What This GPU IS / IS NOT

✅ This IS

✔ A real SIMD GPU compute core
✔ A programmable parallel processor
✔ A verified RTL design
✔ An academic & engineering-grade project

❌ This is NOT

✖ A fabricated chip
✖ A transistor-level GDS layout
✖ A modern gaming GPU
✖ A fake demo


---
``
🛠 Tools & Technologies

🧠 Verilog / SystemVerilog

🧪 EDA Playground

📈 EPWave (Waveform Viewer)

⚙ Icarus Verilog



---
``
🚀 Why This Project Matters

Most “GPU” projects online:

Have no RTL

Have no instruction execution

Have no simulation proof


G-CORE-X1 does.

This project represents the execution engine of a GPU, built and verified honestly.


---
``

🔮 Future Work (Optional)

Warp / thread scheduler

Shared global memory

Cache hierarchy

Graphics pipeline front-end

Performance benchmarking



---

<div align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1200&color=00FFAA&center=true&vCenter=true&width=650&lines=Not+a+toy;Not+copied;Built+from+scratch;Verified+in+simulation" /></div>
---
```
🏁 Final Statement

> G-CORE-X1 is a real, working, multi-core SIMD GPU compute architecture, implemented and verified at RTL level.



No exaggeration.
No copied content.
Just engineering.
```
---
