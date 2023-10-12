from typing import List
import matplotlib.pyplot as plt
from matrix import Matrix
import os


class GerschgorinKreis:
    def __init__(self, matrix: Matrix) -> None:
        self.matrix = matrix
        if not self.matrix.quadratic():
            raise ValueError(f"Matrix must be quadratic, was {self.matrix}")
        self.radii = self.radius()
        self.colors = ["red", "green", "blue", "violet"]

    def radius(self) -> List[int | float]:
        """
        x := a_ii

        r := Summe von j=1 mit j!=i bis n (|a_ij|)

        :return: List[radius] corresponding to diagonal elements a_ii
        """
        radii = []
        for i in range(self.matrix.zeilen):
            radius = 0
            for j in range(self.matrix.spalten):
                if i == j:
                    continue
                a_ij = self.matrix.data[i][j]
                radius += abs(a_ij)
            radii.append(radius)

        return radii

    def plot(self):
        """ Plottet Gerschgorin Kreise """
        if self.radii is None:
            raise ValueError(f"Radien müssen berechnet sein bevor plot() gerufen wird")
        max_radius = max(self.radii)

        fig, ax = plt.subplots()
        font = {'fontname': 'Helvetica'}
        ax.axis("equal")
        ax.set_xlabel("Re(z)", loc="right", **font)
        ax.set_ylabel("Im(z)", loc="top", **font)
        ax.set_title(f"Gerschgorin Kreise zur Matrix {self.matrix}", **font)

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

        cords = []
        for i, radius in enumerate(self.radii):
            center_coordinates = (self.matrix.data[i][i], 0)
            cords.append(center_coordinates)
            circle = plt.Circle(xy=center_coordinates, radius=radius, fill=False, color=self.colors[i])
            ax.add_patch(circle)
            ax.plot(
                center_coordinates[0], center_coordinates[1], 'x', markersize=4, label='Crosses', color=self.colors[i]
            )
        min_x = min(cords, key=lambda x: x[0])[0]
        max_x = max(cords, key=lambda x: x[0])[0]
        ax.set_xlim(min_x - 2, max_x + 2)
        ax.set_ylim((-2 * max_radius, 2 * max_radius))
        plt.show()
        fig.savefig(os.path.join("plots", f"plot_{self.matrix}.svg"), format="svg", dpi=1200)


if __name__ == "__main__":

    werte = [
        [2, 1, 0.5],
        [0.2, 5, 0.7],
        [1, 0, 6]
    ]

    werte2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    m = Matrix(werte)
    g = GerschgorinKreis(m)
    g.plot()
