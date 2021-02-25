import parse
import sys
from dataclasses import dataclass

Intersection = int
Street = str

@dataclass
class Solution:
    schedules: dict[Intersection, dict[Street, int]]

    def __init__(self, sch):
    	self.schedules = sch

    def write_to_file(self, path: str):
        with open(path, 'w') as f:
            print(len(self.schedules), file=f)

            for intersection, schedule in self.schedules.items():
                print(intersection, file=f)
                print(len(schedule), file=f)

                for street_name, seconds in schedule.items():
                    print(street_name, seconds, file=f)


inp = parse.read_file(sys.argv[1])

schedules = {}
for inter, v_calles in inp.interseccion.items():
	i_dict = {}
		
	for c in v_calles:
		i_dict[c] = inp.coches_por_calle[c]

	m = min(i_dict, key=i_dict.get)

	for c, val in inp.interseccion.items():
		i_dict[c] = int(val / m)

	schedules[inter] = i_dict

solution = Solution(schedules)
solution.write_to_file('outputs/{}.txt'.format(input_file_name))


# Semaforo A: 20/35	 4	       *80/Ciclos seg?
# Semáforo B: 10/35    2                    *80
# Semáforo C: 5/35     1  
