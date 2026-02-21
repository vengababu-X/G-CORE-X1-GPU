<div align="center">

# 🚀 G-CORE-X1 GPU  
### 🧠 Multi-Core SIMD GPU Compute Architecture (RTL)

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=900&color=00F7FF&center=true&vCenter=true&width=900&lines=Multi-Core+SIMD+GPU;RTL+Implemented+%7C+Simulated+%7C+Verified;Instruction-Driven+Parallel+Compute;Built+From+Scratch+in+Verilog;Waveform-Verified+Hardware+Design" />

</div>

---

## 🟢 Project Status

```diff
+ RTL DESIGN COMPLETE
+ SIMD VECTOR EXECUTION VERIFIED
+ LOAD / STORE MEMORY IMPLEMENTED
+ MULTI-CORE GPU FUNCTIONAL
+ WAVEFORM-BASED VERIFICATION DONE


---
```

📌 Overview

G-CORE-X1 is a real GPU compute core, implemented at Register Transfer Level (RTL) using Verilog.

This project implements the compute engine of a GPU, focusing on parallel SIMD execution, not graphics output.

It is designed to demonstrate how a GPU works internally:

instruction fetch

vector execution

memory access

multi-core scaling


This is hardware. It is simulated, verified, and reproducible.


---

🎯 What This Project IS

✅ A programmable SIMD GPU compute architecture
✅ A parallel processor with multiple compute units
✅ An RTL-level hardware design
✅ Verified using industry-standard simulation
✅ Suitable for academic, learning, and architecture exploration


---

🚫 What This Project is NOT

❌ Not a graphics card
❌ No HDMI / display output
❌ No rasterizer or texture units
❌ No transistor-level GDS or tape-out
❌ No fake performance charts or FPS claims

```
---

🧩 High-Level Architecture

+-----------------------------------------------------------+
|                       G-CORE-X1 GPU                       |
|                                                           |
|  +------------------ Shared Instruction Memory ----------+|
|  |                                                       ||
|  |   +-------------+       +-------------+              ||
|  |   | Compute CU0 |       | Compute CU1 |              ||
|  |   |-------------|       |-------------|              ||
|  |   | SIMD ALU    |       | SIMD ALU    |              ||
|  |   | Vector RF   |       | Vector RF   |              ||
|  |   | Data Memory |       | Data Memory |              ||
|  |   +-------------+       +-------------+              ||
|  |                                                       ||
|  +-------------------------------------------------------+|
|                                                           |
|        Global Interconnect + Clock Distribution Network   |
+-----------------------------------------------------------+


---
```
🧠 GPU Design Layers

🔹 Layer 0 — SIMD ALU

Multi-lane vector ALU

ADD and MUL operations

Same instruction applied across all lanes


🔹 Layer 1 — Vector Register File

Multiple vector registers

Parallel read/write access

Supplies operands to ALU


🔹 Layer 2 — Instruction Fetch

Program Counter (PC)

Instruction Memory (IMEM)

Autonomous execution (no manual driving)


🔹 Layer 3 — Data Memory

Local per-core memory

LOAD and STORE instructions

Memory-based computation


🔹 Layer 4 — Multi-Core GPU

Multiple compute units instantiated

Shared instruction stream

Parallel execution across cores



---

📜 Instruction Set Architecture (ISA)

Instruction Format (16-bit)

[15:14] Opcode
[13:11] Destination Register
[10:8]  Source Register
[7:0]   Immediate / Address

Supported Instructions

Opcode	Instruction	Description

00	ADD	Vector addition
01	MUL	Vector multiplication
10	LOAD	Load vector from memory
11	STORE	Store vector to memory


Execution Model: SIMD
One instruction → executed across all vector lanes.


---

🧪 Simulation & Verification

Verification is performed using RTL simulation, which is the industry-standard method for validating hardware designs.

Tools Used

Icarus Verilog

EDA Playground

EPWave (waveform viewer)


Verified Behavior

+ Program Counter increments correctly
+ Instructions fetched from IMEM
+ SIMD ALU executes vector operations
+ Register file write-back functions correctly
+ LOAD / STORE memory operations verified
+ Multiple compute units execute in parallel

📈 Waveforms (.vcd) are the simulation graphs
They provide complete functional proof.


---

▶️ How to Use / Run This GPU

Option 1 — Run on EDA Playground (Recommended)

1. Open https://edaplayground.com


2. Select:

Language: SystemVerilog / Verilog

Simulator: Icarus Verilog



3. Paste:

RTL into design.sv

Testbench into testbench.sv



4. Set Top Module:

tb_multi_core


5. Click Run


6. Open EPWave


7. Observe signals:

clk

pc

opcode

alu_out

mem_out

core0.pc

core1.pc




You are now watching a GPU execute instructions.


---

Option 2 — Run Locally (Linux / WSL)

iverilog -g2012 design.sv testbench.sv
vvp a.out
gtkwave dump.vcd


---

🧪 Example Instruction Program

// Example program in Instruction Memory
imem[0] = ADD   R3 = R1 + R2
imem[1] = MUL   R4 = R1 * R2
imem[2] = STORE R4 -> MEM[9]

This demonstrates:

Instruction fetch

SIMD execution

Register write-back

Memory store


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
├── testbench/
│   └── tb_multi_core.sv
│
├── simulations/
│   └── *.vcd
│
├── docs/
│   ├── architecture.md
│   └── diagrams/
│
└── README.md


---
```

🏗 Circuit-Level View (Conceptual)

Instruction Memory → Control Logic

Control Logic → Compute Units

Each Compute Unit contains:

SIMD ALU

Vector Register File

Local Data Memory



This is a block-level circuit schematic, standard in GPU documentation.


---

🏗 Physical Layout (Conceptual)

Floorplan-level organization

Tiled compute units

Shared instruction memory

Global interconnect and clock network


⚠ This represents physical organization, not fabricated silicon.


---

⚠ Limitations

No branch unit

No warp scheduler

No cache hierarchy

No graphics pipeline

No PCIe / host interface

No physical tape-out


These are deliberate exclusions, not flaws.


---

🔮 Future Work

Warp / thread scheduler

Shared global memory

Cache hierarchy

Branch handling

Graphics front-end

Synthesis and P&R flow



---

❓ FAQ

Is this a real GPU?
Yes — a real GPU compute core, not a display GPU.

Does it execute instructions?
Yes — instruction-driven SIMD execution.

Is it verified?
Yes — via RTL simulation and waveforms.

Why no graphics output?
Graphics pipelines are separate subsystems.


---

🏁 Final Statement

G-CORE-X1 is a real, working, multi-core SIMD GPU compute architecture, implemented and verified at RTL level.

No exaggeration.
No copied content.
No fake claims.

Just engineering.

