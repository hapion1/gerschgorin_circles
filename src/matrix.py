from typing import List
import numpy as np


class Matrix:
    def __init__(self, data: List[List[int | float | complex]]) -> None:
        self.zeilen = len(data)  # Anzahl Zeilen
        self.spalten = len(data[0])  # Anzahl Spalten
        self.data = np.array(data)  # Werte[Zeile][Spalte]
        self.determinant = None
        self.eigenwerte = None
        self.eigenvectors = None
        i = 1
        while True:
            try:
                if len(data[0]) != len(data[i]):
                    raise ValueError(
                        f"Column vectors have to have equal length: Vector_0 {data[0]} != Vector_{i} {data[i]}"
                        f"Values: {data = }"
                    )
                i += 1
            except IndexError:
                break

    def __add__(self, other):
        """ Matrix addition """
        if not self.zeilen == other.zeilen or not self.spalten == other.spalten:
            raise ValueError(f"Matrices must have equal dimensions")

        matrix = self.data + other.data
        return matrix

    def __sub__(self, other):
        """ Matrix subtraction """
        if not self.zeilen == other.zeilen or not self.spalten == other.spalten:
            raise ValueError(f"Matrices must have equal dimensions")

        matrix = self.data - other.data
        return matrix

    def __repr__(self) -> str:
        return "\n"+str(self.data)

    def det(self) -> int | float | complex:
        if not self.quadratic():
            raise ValueError(f"Matrix must be quadratic to compute determinant")
        array = self.data
        determinant = np.linalg.det(array)
        self.determinant = determinant
        return determinant

    def quadratic(self) -> bool:
        return self.zeilen == self.spalten

    def eigenvalues(self):
        """
        Eigenvector corresponding to eigenvalues[i] := eigenvectors[:,i]
        :return: Eigenvalues, Eigenvectors
        """
        if not self.quadratic():
            raise ValueError(f"Matrix must be quadratic to compute Eigenvalues")

        if self.eigenwerte and self.eigenvectors:
            return self.eigenvalues, self.eigenvectors

        array = self.data
        eigenvalues, eigenvectors = np.linalg.eig(array)
        self.eigenwerte = eigenvalues
        self.eigenvectors = eigenvectors
        return eigenvalues, eigenvectors


if __name__ == "__main__":
    werte1 = [
        [2, 1, 0.5],
        [0.2, 5, 0.7],
        [1, 0, 6]
    ]

    werte2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix1 = Matrix(werte1)
    matrix2 = Matrix(werte2)

    add = matrix1 + matrix2
    sub = matrix1 - matrix2

    eig = matrix2.eigenvalues()

    det1 = matrix1.det()
    det2 = matrix2.det()

    print(matrix1)
