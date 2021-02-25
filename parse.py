from dataclasses import dataclass
from collections import defaultdict
from typing import Dict, List, Any

@dataclass
class StreetInfo:
    begin: int
    end: int
    time: int

Calle = str
Interseccion = int

@dataclass
class Input:
    D: int
    I: int
    S: int
    V: int
    F: int
    calles: Dict[Calle, StreetInfo]
    coches: Dict[int, List[Calle]]
    interseccion: Dict[Interseccion, List[Calle]]
    coches_por_calle: Any


def read_file(name: str) -> Input:
    with open(name, 'r') as f:
        D, I, S, V, F = [int(x) for x in f.readline().split(' ')]

        calles = dict()
        coches = dict()
        interseccion = defaultdict(list)
        coches_por_calle = defaultdict(int)

        for _ in range(S):
            B, E, name, L = f.readline().split(' ')
            calles[name] = StreetInfo(int(B), int(E), int(L))
            interseccion[E].append(name)

        for i in range(V):
            _, *calles = f.readline().strip().split(' ')
            for calle in calles:
                coches_por_calle[calle] += 1
            coches[i] = calles

    return Input(D,I,S,V,F,calles,coches,interseccion,coches_por_calle)   
    


