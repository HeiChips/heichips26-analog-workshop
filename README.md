# HeiChips26 Analog Workshop

HeiChips 2026 Analog Workshop

> [!IMPORTANT]
> The workshop tutorial is available at: <https://heichips.github.io/heichips26-analog-workshop/>

Table Of Contents

- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [Analog Design](#analog-design)
  - [Open a Schematic](#open-a-schematic)
  - [Run a Simulation](#run-a-simulation)
  - [Edit a Layout](#edit-a-layout)
  - [Verify and Build the Macro](#verify-and-build-the-macro)

## Prerequisites

This repository provides a Nix shell with all the tools required for analog design, digital design and verification.

If you haven't installed Nix yet, please follow LibreLane's documentation: [Nix-based Installation](https://librelane.readthedocs.io/en/latest/installation/nix_installation/index.html).

> [!NOTE]
> The HeiChips VM has Nix already pre-installed.

Now, simply execute `nix-shell` from the root directory of this repository to enable all of the required tools. This must be done every time you open a new shell.

The first time you enable the Nix shell, please run the following two setup targets:

```sh
make clone-pdk      # install the IHP Open PDK for ihp-sg13cmos5l in this repository
make klayout-setup  # install the KLayout plugins in your user directory
```

`clone-pdk` is per repository, it clones the PDK into `IHP-Open-PDK/` next to this file.

`klayout-setup` is per user and only has to be run **once per machine**. It installs the [KLayout Productivity Suite](https://github.com/iic-jku/klayout-productivity-suite) plus the `xsection` tool into `~/.klayout/salt/`, which every KLayout instance of your user account picks up. If you already installed these plugins from another HeiChips or IIC-JKU repository, you can skip this target. Running it again is harmless, it simply reinstalls the packages.

Run `make` (or `make help`) in the root directory to see all available targets.

## Repository Structure

```text
📁 heichips26-analog-workshop/
├─ 📁 config/     Shared tool configuration (.spiceinit for ngspice, klayoutrc for KLayout)
├─ 📁 doc/        Cheatsheets, PDK documentation, and sizing techsweeps
├─ 📁 inverter/   The analog example macro (schematic, testbenches, layout, verification)
├─ 📁 workshop/   Sources of the workshop website
├─ flake.nix      Nix environment with all required tools
├─ Makefile       PDK setup and tool launch targets
└─ README.md      This file
```

## Analog Design

### Open a Schematic

1. First, enable a Nix shell using `nix-shell`.
2. Export `PDK_ROOT` and `PDK`: `export PDK_ROOT=$(pwd)/IHP-Open-PDK && export PDK=ihp-sg13cmos5l`
3. Change the path to the schematic folder of the macro, e.g.
   - `cd inverter/schematic/xschem`
4. Open xschem: `xschem <name of schematic>`, e.g. `xschem inverter.sch`

Starting xschem from that folder picks up its local `xschemrc`, which sources the PDK libraries and adds the macro's schematic and testbench folders to the library path.

> [!TIP]
> If you would like to open the PDK "start page" schematic, run: `xschem --rcfile $PDK_ROOT/$PDK/libs.tech/xschem/xschemrc`

### Run a Simulation

1. First, enable a Nix shell using `nix-shell`.
2. Export `PDK_ROOT` and `PDK`: `export PDK_ROOT=$(pwd)/IHP-Open-PDK && export PDK=ihp-sg13cmos5l`
3. Change the path to the testbench folder of the macro, e.g.
   - `cd inverter/testbenches/xschem`
4. Open xschem: `xschem <name of testbench>`, e.g. `xschem inverter_tb_tran.sch`
5. In the schematic Ctrl + left click: "Simulate"
6. In the schematic Ctrl + left click: "Annotate OP" or "Load waves"

Simulations can also be run non-interactively from the macro folder:

```sh
cd inverter
make sim-xschem                        # run the default testbench (inverter_tb_tran)
make sim-xschem TB=inverter_tb_ac_ol   # run another testbench
make sim-all                           # run all testbenches in sequence
make sim-view-xschem                   # plot the results with Python
```

### Edit a Layout

1. First, enable a Nix shell using `nix-shell`.
2. Export `PDK_ROOT` and `PDK`: `export PDK_ROOT=$(pwd)/IHP-Open-PDK && export PDK=ihp-sg13cmos5l`
3. Start KLayout in edit mode: `make klayout`

Now you can create or open a layout and edit it. The layout of the example macro is `inverter/layout/inverter.gds`.

### Verify and Build the Macro

All verification and build steps are invoked from the macro folder:

```sh
cd inverter
make                # show all available targets
make klayout-verify # DRC and LVS with KLayout
make magic-verify   # DRC, LVS, and PEX with Magic + Netgen
make build-top      # LEF, LIB, Verilog stub, final GDS, and render
make all            # verify, build, and simulate everything
make clean          # delete all generated files and folders
```

See the [inverter README](inverter/README.md) for the complete description of all targets and their parameters.
