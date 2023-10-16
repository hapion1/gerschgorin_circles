import os
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np

from .matrix import Matrix


class GerschgorinKreis:
    def __init__(self, matrix: Matrix) -> None:
        self.matrix = matrix
        if not self.matrix.quadratic():
            raise ValueError(f"Matrix must be quadratic, was {self.matrix}")
        self.radii = self.radius()
        self.colors = ["red", "green", "blue", "violet"]

    def radius(self) -> List[int | float]:
        """
        Calculates radii r_i for Gerschgorin Circles S(a_ii, r_i)

        r := Summe von j=1 mit j<>i bis n (|a_ij|)

        :return: List[radius] corresponding to diagonal elements a_ii
        """
        radii = list()
        for i in range(self.matrix.zeilen):
            radius = 0
            for j in range(self.matrix.spalten):
                if i == j:
                    continue
                a_ij = self.matrix.data[i][j]
                radius += abs(a_ij)
            radii.append(radius)
        return radii

    def plot(self, eigenvalues=False, legend=False) -> None:
        """ Plots Gerschgorin Circles and optionally eigenvalues """
        if self.radii is None:
            raise ValueError(f"Radien müssen berechnet sein bevor plot() gerufen wird")
        max_radius: int | float = max(self.radii)

        fig, ax = plt.subplots()
        font = {'fontname': 'Helvetica'}
        ax.axis("equal")
        ax.set_xlabel("Re(z)", loc="right", **font)
        ax.set_ylabel("Im(z)", loc="top", **font)
        ax.set_title(f"Gerschgorin Circles for Matrix {self.matrix.data}", **font)

        # set the x-spine
        ax.spines['left'].set_position('zero')

        # turn off the right spine/ticks
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()

        # set the y-spine
        ax.spines['bottom'].set_position('zero')

        # turn off the top spine/ticks
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        # arrows at the end of axes
        ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

        cords: List[Tuple[int | float, int | float]] = list()
        for i, radius in enumerate(self.radii):
            if isinstance(self.matrix.data[i][i], complex):
                c: complex = self.matrix.data[i][i]
                center_coordinates: Tuple[float, float] = (c.real, c.imag)
            else:
                center_coordinates: Tuple[int | float, int] = (self.matrix.data[i][i], 0)
            cords.append(center_coordinates)
            circle = plt.Circle(
                xy=center_coordinates, radius=radius, fill=False, color=self.colors[i],
                label=f"S({self.matrix.data[i][i]}, {self.radii[i]})"
            )
            ax.add_patch(circle)
            ax.plot(
                center_coordinates[0], center_coordinates[1], "x", markersize=4, label="Circle Center",
                color=self.colors[i]
            )
        min_x = min(cords, key=lambda x: x[0])[0]
        max_x = max(cords, key=lambda x: x[0])[0]

        # Todo: fix scaling for complex numbers
        if isinstance(min_x, complex) or isinstance(max_x, complex):
            min_x = min_x.real
            max_x = max_x.real

        ax.set_xlim(min_x - 2, max_x + 2)
        ax.set_ylim((-2 * max_radius, 2 * max_radius))

        if eigenvalues:
            eigenwerte: np.ndarray = self.matrix.eig()[0]
            for eig in eigenwerte:
                if isinstance(eig, complex):
                    ax.plot(eig.real, eig.imag, "o", markersize=4, label=f"Eigenvalue {eig:.1f}", color="indigo")
                else:
                    ax.plot(eig, 0, "o", markersize=4, label=f"Eigenvalue {eig:.1f}", color="indigo")
        if legend:
            plt.legend(loc="lower right")
        plt.show()
        dir_path = os.path.join("..", "gerschgorin_plots")
        ensure_directory(dir_path)
        plot_path = os.path.join(dir_path, f"plot_{self.matrix}.svg")
        fig.savefig(plot_path, format="svg", dpi=1200)


def ensure_directory(path: str) -> None:
    if not os.path.isdir(path):
        os.mkdir(path)


if __name__ == "__main__":
    werte = [  # NOQA
        [2, 1, 0.5],
        [0.2, 5, 0.7],
        [1, 0, 6]
    ]

    werte2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    werte3 = [
        [complex("1+1j"), complex("0-1j"), complex("0-0j")],
        [complex("-5-2j"), complex("0-0j"), complex("0-0j")],
        [complex("0-0j"), complex("0-0j"), complex("-1-1j")]
    ]

    m = Matrix(werte3)
    g = GerschgorinKreis(m)
    g.plot(eigenvalues=True, legend=False)
