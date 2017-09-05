import matplotlib.pyplot as plt
import pandas as pd

# Pandas :)
df = pd.read_csv('exoplanets_subset.txt', header=None, sep='\s+', comment='#',
                 names=['Mass', 'Radius', 'Period', 'Method', "Disc. Year"])

# The way the assignments asks
data = open('exoplanets_subset.txt', 'r')
lines = data.readlines()

Rjup = []
Pday = []

# Read data from file, and put it into individual lists
for line in lines:
    if not line.startswith('#'):		# Skip lines that start with #
        x = line.split()  # breaks the data up by spaces in each line
        Rjup.append(float(x[1]))  # Add to the array the correct element
        Pday.append(float(x[2]))

print(Rjup, Pday)

# Total number of planets
planets = len(Rjup)  # len(df)
print('Total number of planets:', planets)


# convert from Rjup ro Rearth
def Rjuptoearth(Rjup):
    Re = Rjup*11.209
    return Re

# Populate a list using conversion function
Re = [Rjuptoearth(Rjup[i]) for i in range(len(Rjup))]

df['Re'] = df["Radius"] * 11.209

# How many found via imaging?
image = df[df['Method'] == 'imaging']
print(len(image))

# create separate points for transit and RV
transit = df[df['Method'] == 'transit']
RV = df[df['Method'] == 'RV']

# ---- Create the Figure -----
fig, (ax1, ax2) = plt.subplots(1, 2)  # Makes two plots separated on the same page

# First fig.- Hist of radii with 20 bins
ax1.hist(df['Re'], bins=20, color='#17becf', histtype='step', edgecolor='k')
ax1.set_xlabel('Radius (R$_{Earth}$)')
ax1.set_ylabel('Number of Planets')
ax1.title.set_text('Planetary Radii')

# Second fig.- radii vs period dots as markers use plot meths
t = ax2.plot(transit['Period'], transit['Re'], marker='.', ls='None', color='k', ms=2)  # Dude why not plt.scatter?!
# ax2.scatter(Pday, Rjup, s=10)
r = ax2.plot(RV['Period'], RV['Re'], marker='o', ls='None', color='red', ms=3)  # ms= markersise
im = ax2.plot(image['Period'], image['Re'], marker='^', ls='None', color='blue', ms=3)
ax2.set_xlabel('Period (days)')
ax2.set_ylabel('Radius (R$_{Earth}$)')
ax2.set_xscale('log')  # changing the scale after the fact instead of ax2.semilogx
ax2.axvline(x=365, color='red', ls=':')
ax2.axhline(y=1, color='k', ls='--')
ax2.title.set_text('Radius vs Period')
ax2.legend(["transit", 'RV', 'Imaging'])

plt.tight_layout()  # Fixes labels so they fit on the figure nicely, instead of using gcf
plt.show()
plt.savefig('Module2.png')
