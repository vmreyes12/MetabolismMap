#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


###Import all of your files as data frames, combine metadata, and output searchable hit files###
#Manually change genome_id column in excel file
os.chdir('/home/victor/Documents/faa_loops')
metadata = pd.read_excel('genome_metadata.xlsx')
os.chdir('/home/victor/JGI_data_output')
idrA_hits = pd.read_excel('idrA_target_file.xlsx')
ptxD_hits = pd.read_excel('ptxD_target_file.xlsx')
pcrA1_hits = pd.read_excel('pcrA1_target_file.xlsx')
pcrA2_hits = pd.read_excel('pcrA2_target_file.xlsx')

#Reset indices
idrA_hits = idrA_hits.set_index('genome_id').reset_index()
ptxD_hits = ptxD_hits.set_index('genome_id').reset_index()
pcrA1_hits = pcrA1_hits.set_index('genome_id').reset_index()
pcrA2_hits = pcrA2_hits.set_index('genome_id').reset_index()

#Import metadata
metadata = metadata.set_index('genome_id').reset_index()

#Merge metadata with genome ids 
final_idrA = metadata.merge(idrA_hits, how='inner', on='genome_id')
final_ptxD = metadata.merge(ptxD_hits, how='inner', on='genome_id')
final_pcrA1 = metadata.merge(pcrA1_hits, how='inner', on='genome_id')
final_pcrA2 = metadata.merge(pcrA2_hits, how='inner', on='genome_id')

f = ['final_idrA', 'final_ptxD', 'final_pcrA1', 'final_pcrA2']

#Export combined dataframes
final_idrA.to_excel('final_idrA.xlsx')
final_ptxD.to_excel('final_ptxD.xlsx')
final_pcrA1.to_excel('final_pcrA1.xlsx')
final_pcrA2.to_excel('final_pcrA2.xlsx')


plt.rcParams["font.family"] = "Arial"


##SPLIT THE TAXONOMY##
#There is a lot of taxonomic data, you can choose whatever is to your interest
fi = final_idrA.ecosystem.str.split('__',expand=True)
fi
Domain_idrA = fi[1].str.replace(r';p', '')
Phylum_idrA = fi[2].str.replace(r';c', '')
Class_idrA = fi[3].str.replace(r';o', '')
Order_idrA = fi[4].str.replace(r';f', '')
Family_idrA = fi[5].str.replace(r';g', '')
Genus_idrA = fi[6].str.replace(r';s', '')
Species_idrA = fi[7]

fp = final_ptxD.ecosystem.str.split('__',expand=True)
fp
Domain_ptxD = fp[1].str.replace(r';p', '')
Phylum_ptxD = fp[2].str.replace(r';c', '')
Class_ptxD = fp[3].str.replace(r';o', '')
Order_ptxD = fp[4].str.replace(r';f', '')
Family_ptxD = fp[5].str.replace(r';g', '')
Genus_ptxD = fp[6].str.replace(r';s', '')
Species_ptxD = fp[7]

fc = final_pcrA1.ecosystem.str.split('__',expand=True)
fc
Domain_pcrA1 = fc[1].str.replace(r';p', '')
Phylum_pcrA1 = fc[2].str.replace(r';c', '')
Class_pcrA1 = fc[3].str.replace(r';o', '')
Order_pcrA1 = fc[4].str.replace(r';f', '')
Family_pcrA1 = fc[5].str.replace(r';g', '')
Genus_pcrA1 = fc[6].str.replace(r';s', '')
Species_pcrA1 = fc[7]

fd = final_pcrA2.ecosystem.str.split('__',expand=True)
fd
Domain_pcrA2 = fd[1].str.replace(r';p', '')
Phylum_pcrA2 = fd[2].str.replace(r';c', '')
Class_pcrA2 = fd[3].str.replace(r';o', '')
Order_pcrA2 = fd[4].str.replace(r';f', '')
Family_pcrA2 = fd[5].str.replace(r';g', '')
Genus_pcrA2 = fd[6].str.replace(r';s', '')
Species_pcrA2 = fd[7]

#Create Phylum level taxonomy. If different taxonomic rank is desired, change the variable in Counter() function#
from collections import Counter
Phy_idrA = Counter(Phylum_idrA)
Phy_idrA = {k: v for k, v in sorted(Phy_idrA.items(), key=lambda item: item[1], reverse=False)}

from collections import Counter
Phy_ptxD = Counter(Phylum_ptxD)
Phy_ptxD = {k: v for k, v in sorted(Phy_ptxD.items(), key=lambda item: item[1], reverse=False)}

from collections import Counter
Phy_pcrA1 = Counter(Phylum_pcrA1)
Phy_pcrA1 = {k: v for k, v in sorted(Phy_pcrA1.items(), key=lambda item: item[1], reverse=False)}

from collections import Counter
Phy_pcrA2 = Counter(Phylum_pcrA2)
Phy_pcrA2 = {k: v for k, v in sorted(Phy_pcrA2.items(), key=lambda item: item[1], reverse=False)}

idrA = pd.DataFrame(list(Phy_idrA.items()),columns=['Phylum', 'Count'])
idrA['Enzyme'] = 'purple' #idrA
ptxD = pd.DataFrame(list(Phy_ptxD.items()),columns=['Phylum', 'Count'])
ptxD['Enzyme'] = 'orange' #ptxD
pcrA1 = pd.DataFrame(list(Phy_pcrA1.items()),columns=['Phylum', 'Count'])
pcrA1['Enzyme'] = 'green' #pcrA1
pcrA2 = pd.DataFrame(list(Phy_pcrA2.items()),columns=['Phylum', 'Count'])
pcrA2['Enzyme'] = 'green' #pcrA2
combined_taxonomy = pd.concat([idrA,  ptxD, pcrA1, pcrA2])



##Draw Phylum level taxonomy barcharts##
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(15,15),sharey=False)

ax1.barh(range(len(Phy_pcrA1)), list(Phy_pcrA1.values()), align='center', color='Green')
ax1.set_yticks(range(len(Phy_pcrA1)))
ax1.set_yticklabels(list(Phy_pcrA1.keys()))
ax1.set_title('PcrA1',size=20)

ax2.barh(range(len(Phy_pcrA2)), list(Phy_pcrA2.values()), align='center', color='Darkgreen')
ax2.set_yticks(range(len(Phy_pcrA2)))
ax2.set_yticklabels(list(Phy_pcrA2.keys()))
ax2.set_title('PcrA2',size=20)

ax3.barh(range(len(Phy_idrA)), list(Phy_idrA.values()), align='center', color='Purple')
ax3.set_yticks(range(len(Phy_idrA)))
ax3.set_yticklabels(list(Phy_idrA.keys()), size=12)
ax3.set_title('IdrA',size=20)

ax4.barh(range(len(Phy_ptxD)), list(Phy_ptxD.values()), align='center', color='Orange')
ax4.set_yticks(range(len(Phy_ptxD)))
ax4.set_yticklabels(list(Phy_ptxD.keys()))
ax4.set_title('PtxD',size=20)

plt.suptitle('Taxonomy of Genomes with Metabolism Present', size=24, y=1.1)
plt.ylabel('Phylum')
plt.tight_layout()
plt.style.use('seaborn-poster')
plt.savefig('Combined_taxonomy.svg',bbox_inches='tight',dpi=300)
plt.show()



##Draw circular taxonomy chart##
# set figure size
plt.figure(figsize=(30,15))

# plot polar axis
ax = plt.subplot(111, polar=True)

# remove grid
plt.axis('off')

# Set the coordinates limits
upperLimit = 100
lowerLimit = 30

# Compute max and min in the dataset
max = combined_taxonomy['Count'].max()

# Let's compute heights: they are a conversion of each item value in those new coordinates
# In our example, 0 in the dataset will be converted to the lowerLimit (10)
# The maximum will be converted to the upperLimit (100)
slope = (max - lowerLimit) / max
combined_taxonomy['heights'] = slope * combined_taxonomy.Count + lowerLimit

# Compute the width of each bar. In total we have 2*Pi = 360°
combined_taxonomy['width'] = 2*np.pi / len(combined_taxonomy.index)

# Compute the angle each bar is centered on:
indexes = list(range(1, len(combined_taxonomy.index)+1))
combined_taxonomy['angles'] = [element * width for element in indexes]


for label, count, heights, angles, width, color in zip(combined_taxonomy["Phylum"], combined_taxonomy["Count"], combined_taxonomy['heights'], combined_taxonomy['angles'], combined_taxonomy['width'], combined_taxonomy["Enzyme"]):
    # Draw bars
    count = str(count)
    bars = ax.bar(
        x=angles, 
        height=heights, 
        width=width, 
        bottom=lowerLimit,
        linewidth=2,
        color=color,
        edgecolor="white")
    rotation = np.rad2deg(angles)
    labelPadding = 4
    # Flip some labels upside down
    alignment = ""
    if angles >= np.pi/2 and angles < 3*np.pi/2:
        alignment = "right"
        rotation = rotation + 180
    else: 
        alignment = "left"
    # Finally add the labels
    ax.text(
        x=angles, 
        y=lowerLimit + heights + labelPadding, 
        s=label + ' (' + count + ')',
        fontsize=12,
        ha=alignment, 
        va='center', 
        rotation=rotation, 
        rotation_mode="anchor") 
         #little space between the bar and the label
plt.savefig('metabolism_phyla_circular.svg',bbox_inches='tight',dpi=300)


##Draw Habitat Barcharts##

habitat_idrA = Counter(final_idrA.habitat)
habitat_idrA = {k: v for k, v in sorted(habitat_idrA.items(), key=lambda item: item[1], reverse=False)}

habitat_ptxD = Counter(final_ptxD.habitat)
habitat_ptxD = {k: v for k, v in sorted(habitat_ptxD.items(), key=lambda item: item[1], reverse=False)}

habitat_pcrA = Counter(final_pcrA.habitat)
habitat_pcrA = {k: v for k, v in sorted(habitat_pcrA.items(), key=lambda item: item[1], reverse=False)}

f, (ax2) = plt.subplots(1, 1,figsize=(7,7),sharey=False)

ax1.barh(range(len(habitat_pcrA)), list(habitat_pcrA.values()), align='center', color='Purple')
ax1.set_yticks(range(len(habitat_pcrA)))
ax1.set_yticklabels(list(habitat_pcrA.keys()), size=12)
ax1.set_xlabel('Number of Genomes', size=18)
ax1.set_ylabel('Habitat', size=18)
ax1.set_title('PcrA',size=20)

ax2.barh(range(len(habitat_idrA)), list(habitat_idrA.values()), align='center', color='Purple')
ax2.set_yticks(range(len(habitat_idrA)))
ax2.set_yticklabels(list(habitat_idrA.keys()), size=12)
ax2.set_xlabel('Number of Genomes', size=18)
ax2.set_title('IdrA',size=20)

ax3.barh(range(len(habitat_ptxD)), list(habitat_ptxD.values()), align='center', color='Orange')
ax3.set_yticks(range(len(habitat_ptxD)))
ax3.set_yticklabels(list(habitat_ptxD.keys()))
ax3.set_xlabel('Number of Genomes', size=18)
ax3.set_title('PtxD',size=20)

plt.suptitle('Locations where metabolisms are found', size=24, y=1.1)
plt.tight_layout()
plt.style.use('seaborn-white')
plt.savefig('Habitats.svg',bbox_inches='tight',dpi=300)
plt.show()


##ECOSYSTEM TYPE##
ecosystem_idrA = Counter(final_idrA.ecosystem_type)
ecosystem_idrA = {k: v for k, v in sorted(ecosystem_idrA.items(), key=lambda item: item[1], reverse=False)}

ecosystem_ptxD = Counter(final_ptxD.ecosystem_type)
ecosystem_ptxD = {k: v for k, v in sorted(ecosystem_ptxD.items(), key=lambda item: item[1], reverse=False)}

ecosystem_pcrA = Counter(final_pcrA.ecosystem_type)
ecosystem_pcrA = {k: v for k, v in sorted(ecosystem_pcrA.items(), key=lambda item: item[1], reverse=False)}

f, (ax2) = plt.subplots(1, 1,figsize=(7,7),sharey=False)

ax1.barh(range(len(ecosystem_pcrA)), list(ecosystem_pcrA.values()), align='center', color='Purple')
ax1.set_yticks(range(len(ecosystem_pcrA)))
ax1.set_yticklabels(list(ecosystem_pcrA.keys()), size=12)
ax1.set_xlabel('Number of Genomes', size=18)
ax1.set_ylabel('Ecosystem', size=18)
ax1.set_title('PcrA',size=20)

ax2.barh(range(len(ecosystem_idrA)), list(ecosystem_idrA.values()), align='center', color='Purple')
ax2.set_yticks(range(len(ecosystem_idrA)))
ax2.set_yticklabels(list(ecosystem_idrA.keys()), size=12)
ax2.set_xlabel('Number of Genomes', size=18)
ax2.set_title('IdrA',size=20)

ax3.barh(range(len(ecosystem_ptxD)), list(ecosystem_ptxD.values()), align='center', color='Orange')
ax3.set_yticks(range(len(ecosystem_ptxD)))
ax3.set_yticklabels(list(ecosystem_ptxD.keys()))
ax3.set_xlabel('Number of Genomes', size=18)
ax3.set_title('PtxD',size=20)

plt.suptitle('Locations where metabolisms are found', size=24, y=1.1)
plt.tight_layout()
plt.style.use('seaborn-white')
plt.savefig('Ecosystems.svg',bbox_inches='tight',dpi=300)
plt.show()

###Draw Distribution Maps##
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import seaborn as sns
import pkg_resources
import matplotlib.pyplot as plt
from matplotlib.cm import cool
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

#This piece of the code will take the longitude/latitudes displayed earlier and make them a list
lonlat_idrA = []
for item in final_idrA.index: 
    name, lon, lat, eco = final_idrA['genome_id'][item], final_idrA['longitude'][item],final_idrA['latitude'][item],final_idrA['ecosystem_type'][item]
    lonlat_idrA.append(name)
    
lonlat_ptxD = []
for item in final_ptxD.index: 
    name, lon, lat, eco = final_ptxD['genome_id'][item], final_ptxD['longitude'][item],final_ptxD['latitude'][item],final_ptxD['ecosystem_type'][item]
    lonlat_ptxD.append(name)
    
lonlat_pcrA = []
for item in final_pcrA1.index: 
    name, lon, lat, eco = final_pcrA1['genome_id'][item], final_pcrA1['longitude'][item],final_pcrA1['latitude'][item],final_pcrA1['ecosystem_type'][item]
    lonlat_pcrA.append(name)
    
for item in final_pcrA2.index: 
    name, lon, lat, eco = final_pcrA2['genome_id'][item], final_pcrA2['longitude'][item],final_pcrA2['latitude'][item],final_pcrA2['ecosystem_type'][item]
    lonlat_pcrA.append(name)
    
len(final_idrA['ecosystem_type'].unique())
uniq_eco_idrA = list(final_idrA['ecosystem_type'].unique())
uniq_eco_ptxD = list(final_ptxD['ecosystem_type'].unique())
uniq_eco_pcrA1 = list(final_pcrA1['ecosystem_type'].unique())
uniq_eco_pcrA2 = list(final_pcrA2['ecosystem_type'].unique())
uniq_eco = uniq_eco_idrA + uniq_eco_ptxD + uniq_eco_pcrA1 + uniq_eco_pcrA2
set(uniq_eco)

final_idrA = final_idrA.assign(Marker='^', color='purple')
final_ptxD = final_ptxD.assign(Marker='s', color='orange')
final_pcrA1 = final_pcrA1.assign(Marker='o', color='green')
final_pcrA2 = final_pcrA2.assign(Marker='o', color='green')

hits = pd.concat([final_idrA, final_ptxD, final_pcrA1, final_pcrA2])
ecosystem = pd.DataFrame(hits['ecosystem_type'])
ecosystem['color_eco'] = ecosystem['ecosystem_type'].apply(lambda x : color_map[x])
hits_color = pd.concat([ecosystem, hits], axis=1, sort=False)
hits_color = hits_color.reset_index()

# The following two lines generate custom fake lines that will be used as legend entries:

legend_elements_2 = [Line2D([0], [0], marker='^', color='w',markersize=12, label='IdrA', markerfacecolor='purple'),
                   Line2D([0], [0], marker='s', color='w',markersize=12, label='PtxD', markerfacecolor='orange'),
                    Line2D([0], [0], marker='o', color='w',markersize=12, label='PcrA', markerfacecolor='green')]


###This part of the analysis allows for drawing a map with hit data###
#Make a dataframe with hit coordinates and total counts at coordinate
#hit_latitudes = IRC_df_indi[['Longitude [degrees East]','Latitude [degrees North]','Raw_count','Hit_count']].reset_index()

###This is the code for making the map###
plt.figure(figsize=(20,8))
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=0))

for item in hits_color.index: 
    name, lon, lat, eco, mark = hits_color['genome_id'][item], hits_color['longitude'][item],hits_color['latitude'][item],hits_color['color'][item],hits_color['Marker'][item]
    plt.scatter([lon], [lat],
             color=eco, marker=mark, s=75, linewidths=1, edgecolor='black', alpha=1.0,
             transform=ccrs.PlateCarree())

# make the map global rather than have it zoom in to
# the extents of any plotted data
ax.set_global()
ax.stock_img()
ax.coastlines()
leg2 = ax.legend(handles=legend_elements_2,loc='lower center',bbox_to_anchor=(0.5, -0.20),fontsize=14, ncol=3, title = 'Marker Gene',title_fontsize=20)
ax.add_artist(leg2)
ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())

labels = [item.get_text() for item in ax.get_yticklabels()]
labels = [-90, -60, -30, 0, 30, 60, 90]
ax.set_yticklabels(labels)

#plt.title('Global Hotspots for Iodate Reduction Cluster Genes', size=36, y=1.05)


plt.style.use('seaborn-white')
plt.savefig('metabolism_distro.svg',bbox_inches='tight',dpi=300)
plt.show()
