#!/usr/bin/env python

import matplotlib.pyplot as plt

datafile = open('exoplanets_subset.txt', 'r')
lines = datafile.readlines()

Rjup = []
Pday = []
Discovery = []
Rjup_transit, Pday_transit = [], []
Rjup_RV, Pday_RV = [], []
Rjup_imaging, Pday_imaging = [], []

# Read data from file, and put it into individual lists
for line in lines:
    if not line.startswith('#'):  # Skip lines that start with #
        a = line.split()
        Rjup.append(float(a[1]))
        Pday.append(float(a[2]))
        Discovery.append(a[3])
        if a[3] == 'transit':
            Rjup_transit.append(float(a[1]))
            Pday_transit.append(float(a[2]))
        elif a[3] == 'RV':
            Rjup_RV.append(float(a[1]))
            Pday_RV.append(float(a[2]))
        elif a[3] == 'imaging':
            Rjup_imaging.append(float(a[1]))
            Pday_imaging.append(float(a[2]))

print('Number detected by transit:', len(Rjup_transit))
print('Number detected by imaging:', len(Rjup_RV))
print('Number detected by imaging:', len(Rjup_imaging))
print('Total number of planets in sample:', len(Rjup))


# Function to convert Jupiter radii to Earth Radii: Rj = 11.2 Re
def Rj_to_Re(R_jup):
    R_earth = R_jup * 11.2
    return R_earth


# Create a new list of planet radii in units of Earth radii, using list comprehension
Re = [Rj_to_Re(Rjup[i]) for i in range(len(Rjup))]
Re_transit = [Rj_to_Re(Rjup_transit[i]) for i in range(len(Rjup_transit))]
Re_RV = [Rj_to_Re(Rjup_RV[i]) for i in range(len(Rjup_RV))]
Re_imaging = [Rj_to_Re(Rjup_imaging[i]) for i in range(len(Rjup_imaging))]

# Plot the data
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.hist(Re, bins=20, histtype='step', edgecolor='k')
ax1.set_title('Planetary Radii')
ax1.set_xlabel('Radius [Earth Radii]')
ax1.set_ylabel('Number of planets')

ax2.plot(Pday_transit, Re_transit, marker='.', color='k', ls='None', markersize=2, label='transit')
ax2.plot(Pday_RV, Re_RV, marker='o', color='r', ls='None', alpha=0.5, markersize=3, label='RV')
ax2.plot(Pday_imaging, Re_imaging, marker='^', color='b', ls='None', alpha=0.5, markersize=3, label='imaging')
ax2.set_xscale('log')
ax2.axhline(y=1, linewidth=1, color='k', ls='--')
ax2.axvline(x=365, linewidth=1, color='r', ls=':')
ax2.set_title('Radius vs Period')
ax2.set_xlabel('Period [days]')
ax2.set_ylabel('Radius [Earth Radii]')
ax2.legend()

plt.tight_layout()
plt.show()
