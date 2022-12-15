#%% Imports for solving puzzle
from pprint import pp
from pathlib import Path
from scanf import scanf


#%% Part 1, test
lines = [i.strip() for i in Path('day15_test.txt').read_text().splitlines()]
sensors = []
beacons = []
for line in lines:
    sx, sy, bx, by = scanf('Sensor at x=%i, y=%i: closest beacon is at x=%i, y=%i', line)
    sensors.append((sx, sy))
    beacons.append((bx, by))

all_xs = [s[0] for s in sensors] + [b[0] for b in beacons]
all_ys = [s[1] for s in sensors] + [b[1] for b in beacons]
xmin = min(all_xs)
xmax = max(all_xs)
ymin = min(all_ys)
ymax = max(all_ys)

y = 10


def mandist(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])


# For each sensor, construct range of necessarily 'empty' spots for a given row
# Put all the ranges into a set
# For each spot in the row, check if it's in the set, mark/print/count accordingly


i = 6
bx, by = beacons[i]
sx, sy = sensors[i]
beacon = beacons[i]
sensor = sensors[i]

dx = abs(bx-sx)
dy = abs(by-sy)
minx_no_beacon = sx - (dx+dy-abs(sy-y))
max_no_beacon = sx + (dx+dy-abs(sy-y))
12 in range(minx_no_beacon, max_no_beacon+1)



#%% Part 1, puzzle


#%%


# %% Part 2, test


# %% Part 2, puzzle
