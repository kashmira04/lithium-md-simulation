from ase.build import bulk
from ase.calculators.lj import LennardJones
from ase.optimize import FIRE
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io import write
from ase import units

# Build lithium crystal
atoms = bulk('Li', 'bcc', a=3.5)
atoms = atoms.repeat((5,5,5))

# Attach potential
atoms.calc = LennardJones()

# Relax structure first
print("Relaxing structure...")
opt = FIRE(atoms)
opt.run(fmax=0.01)

# Assign velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Smaller timestep
dyn = VelocityVerlet(atoms, timestep=0.1 * units.fs)

frames = []

print("Starting stable MD simulation...")

for step in range(20000):

    dyn.run(1)

    # save every 10th frame
    if step % 10 == 0:
        frames.append(atoms.copy())

    if step % 1000 == 0:

        epot = atoms.get_potential_energy()
        ekin = atoms.get_kinetic_energy()

        print(f"Step {step}")
        print(f"Potential Energy: {epot:.3f} eV")
        print(f"Kinetic Energy: {ekin:.3f} eV")
        print(f"Total Energy: {(epot + ekin):.3f} eV")
        print("-----------------------------")

# Save trajectory
write("stable_li_md.xyz", frames)

print("Stable MD simulation complete")