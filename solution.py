from dataclasses import dataclass

Intersection = int
Street = str

@dataclass
class Solution:
    schedules: dict[Intersection, dict[Street, int]]

    def write_to_file(self, path: str):
        with open(path, 'w') as f:
            print(len(self.schedules), file=f)

            for intersection, schedule in self.schedules.items():
                print(intersection, file=f)
                print(len(schedule), file=f)

                for street_name, seconds in schedule.items():
                    print(street_name, seconds, file=f)