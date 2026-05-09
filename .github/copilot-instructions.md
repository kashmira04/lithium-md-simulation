# AI Coding Guidelines for Lithium MD Project

## Project Overview
This is a molecular dynamics simulation project for lithium crystal structures using the Atomic Simulation Environment (ASE). The workflow involves creating crystal structures, relaxing them, and running MD simulations with Lennard-Jones potentials.

## Key Dependencies
- **ASE 3.26.0**: Core library for atomic simulations, structure building, calculators, and I/O
- **NumPy, SciPy, Matplotlib**: For numerical computations and visualization

## Common Patterns
- **Structure Creation**: Use `ase.build.bulk('Li', 'bcc', a=3.5)` for BCC lithium, then `repeat((n,n,n))` for supercells
- **Calculators**: Attach `LennardJones()` for simple potentials; access energies via `atoms.get_potential_energy()`
- **Optimization**: Use `FIRE` optimizer with `opt.run(fmax=0.01)` for structure relaxation
- **MD Simulation**: Initialize velocities with `MaxwellBoltzmannDistribution(atoms, temperature_K=T)`, run with `VelocityVerlet(atoms, timestep=0.1 * units.fs)`
- **I/O**: Save structures as `.xyz` files using `ase.io.write(filename, atoms)`; trajectories as lists of `atoms.copy()`

## Workflow Commands
- Activate environment: `source venv/bin/activate`
- Run structure creation: `python create_lithium.py`
- Run relaxation: `python relax_lithium.py`
- Run MD: `python run_md.py` (long-running, ~20k steps)
- View results: Open `.xyz` files in molecular viewers (e.g., VMD, OVITO)

## File Structure
- `*_lithium.py`: Simulation scripts (creation, relaxation, MD)
- `*.xyz`: Atomic structure files (input/output)
- `*.traj`: Trajectory files (ASE format)
- `venv/`: Python virtual environment with ASE installed

## Conventions
- Use `units.fs` for femtosecond timesteps
- Print energies in eV with 3 decimal places
- Save every 10th frame for trajectories to manage file size
- Log progress every 1000 steps during MD runs

## Key Files
- `run_md.py`: Exemplifies full MD workflow with energy logging
- `relax_lithium.py`: Shows structure optimization pattern
- `create_lithium.py`: Basic structure generation