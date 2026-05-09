from ase.build import bulk
from ase.calculators.lj import LennardJones
from ase.optimize import FIRE
from ase.io import write

# Build lithium BCC crystal
atoms = bulk('Li', 'bcc', a=3.5)

# Repeat unit cell
atoms = atoms.repeat((5,5,5))

# Attach Lennard-Jones potential
atoms.calc = LennardJones()

# FIRE relaxation
opt = FIRE(atoms)

print("Starting relaxation...")

opt.run(fmax=0.01)

print("Relaxation complete")

# Print final energy
print("Final energy:", atoms.get_potential_energy())

# Save relaxed structure
write('relaxed_lithium.xyz', atoms)

print("Relaxed structure saved")