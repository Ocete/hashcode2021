import parse
import sys
from dataclasses import dataclass
from typing import Dict

Intersection = int
Street = str

@dataclass
class Solution:
    schedules: Dict[Intersection, Dict[Street, int]]

    def __init__(self, sch):
        self.schedules = sch

    def write_to_file(self, path: str, inp):
        with open(path, 'w') as f:
            print(len(self.schedules), file=f)

            for intersection, schedule in self.schedules.items():
                print(intersection, file=f)
                print(len(schedule), file=f)

                zipped = [(inp.coches_iniciales[street_name], street_name, seconds) \
                	for street_name, seconds in schedule.items() ]

                #zipped = sorted(zipped, reverse=True)

                for _, street_name, seconds in zipped:
                    print(street_name, seconds, file=f)


inp = parse.read_file(sys.argv[1])

schedules = {}
for inter, v_calles in inp.interseccion.items():
    i_dict = {}
        
    for c in v_calles:
        if c in inp.coches_por_calle:
            i_dict[c] = inp.coches_por_calle[c]

    if not i_dict.values():
        continue

    m = min(i_dict.values())

    for c, n_coches in i_dict.items():
        i_dict[c] = int(n_coches / m)

        # Test for D
        i_dict[c] = 1


    schedules[inter] = i_dict

solution = Solution(schedules)
solution.write_to_file('../outputs/{}'.format(sys.argv[1]), inp)


# Semaforo A: 20/35     4           *80/Ciclos seg?
# Semáforo B: 10/35    2                    *80
# Semáforo C: 5/35     1  
