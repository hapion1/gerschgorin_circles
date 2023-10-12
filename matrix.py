from typing import List


class Matrix:
    def __init__(self, data: List[List[int | float | complex]]):
        self.zeilen = len(data)         # Anzahl Zeilen
        self.spalten = len(data[0])     # Anzahl Spalten
        self.data = data                # Werte[Zeile][Spalte]
        i = 1
        while True:
            try:
                if len(data[0]) != len(data[i]):
                    raise ValueError(
                        f"Spaltenvektoren müssen gleiche Länge haben: Vektor_0 {data[0]} != Vektor_{i} {data[i]}"
                        f"Werte: {data = }"
                    )
                i += 1
            except IndexError:
                break

    def __repr__(self):
        return str(self.data)

    def quadratic(self):
        return self.zeilen == self.spalten


if __name__ == "__main__":
    werte = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = Matrix(werte)
    print(matrix)
