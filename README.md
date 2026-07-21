# HeiChips26 Analog Workshop

HeiChips 2026 Analog Workshop

Table Of Contents

- [Prerequisites](#prerequisites)
- [Analog Design](#analog-design)

## Prerequisites

This template provides a Nix shell with all the tools required for analog design, digital design and verification.

If you haven't installed Nix yet, please follow LibreLane's documentation: [Nix-based Installation](https://librelane.readthedocs.io/en/latest/installation/nix_installation/index.html).

> [!NOTE]
> The HeiChips VM has Nix already pre-installed.

Now, simply execute `nix-shell` from the root directory of this repository to enable all of the required tools. This must be done every time you open a new shell.

The first time you enable the Nix shell, please run `make clone-pdk` to install the IHP Open PDK for ihp-sg13cmos5l in this repository.

## Analog Design

### Open a Schematic

1. First, enable a Nix shell using `nix-shell`.
2. Export `PDK_ROOT` and `PDK`: `export PDK_ROOT=$(pwd)/IHP-Open-PDK && export PDK=ihp-sg13cmos5l`
3. Change the path to the schematic or testbench folder of the macro, e.g.
  - `cd macros/heichips26_analog_project/macros/inverter/schematic/xschem`
  - `cd macros/heichips26_analog_project/schematic/xschem`
4. Open xschem: `xschem <name of schematic>`, e.g. `xschem inverter.sch`

### Run a Simulation

1. First, enable a Nix shell using `nix-shell`.
2. Export `PDK_ROOT` and `PDK`: `export PDK_ROOT=$(pwd)/IHP-Open-PDK && export PDK=ihp-sg13cmos5l`
3. Change the path to the schematic or testbench folder of the macro, e.g.
  - `cd macros/heichips26_analog_project/macros/inverter/testbenches/xschem`
  - `cd macros/heichips26_analog_project/schematic/xschem`
4. Open xschem: `xschem <name of testbench>`, e.g. `xschem inverter_tb_tran.sch`
6. In the schematic Ctrl + left click: "Simulate"
7. In the schematic Ctrl + left click: "Annotate OP" or "Load waves"

### Edit a Layout

1. First, enable a Nix shell using `nix-shell`.
2. Export `PDK_ROOT` and `PDK`: `export PDK_ROOT=$(pwd)/IHP-Open-PDK && export PDK=ihp-sg13cmos5l`
3. Start KLayout in edit mode: `make klayout`

Now you can create or open a layout and edit it.
