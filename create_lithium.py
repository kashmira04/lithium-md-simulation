from ase.build import bulk
from ase.io import write

# Build lithium crystal
li = bulk('Li', 'bcc', a=3.5)

# Repeat unit cell
li = li.repeat((5,5,5))

print(li)
print("Number of atoms:", len(li))

# Save structure
write('lithium.xyz', li)

print("Structure saved as lithium.xyz")