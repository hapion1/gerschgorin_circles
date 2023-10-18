# Gergschgorin Circles

Python implementation of Gerschgorin Circles theorem to estimate Eigenvalues.
For reference see [Gerschgorin Circle Theorem](https://en.wikipedia.org/wiki/Gershgorin_circle_theorem).
Gerschgorin Circles are sometimes called Gerschgorin Discs.

## Installation

From Git:

```
pip install git+<git.url>
```

## Example

The focal utility of this package is the `plot()` method of the `GerschgorinCircle` class.

### Example for 3x3 Matrix with real numbers

```
from gerschgorin_circles import matrix, gerschgorin

# create Matrix
m = matrix.Matrix(
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]   
)

g = gerschgorin.GerschgorinCircle(g)
g.plot(eigenvalues=True, legend=True)
```

Output:

![Gerschgorin Circles 1](./gerschgorin_plots/plot_%0A%5B%5B1%202%203%5D%0A%20%5B4%205%206%5D%0A%20%5B7%208%209%5D%5D.svg)


### PLOT DIRECTORY

If when calling `plot()` with the keyword argument `save_plot=True` the package automatically creates a directory where the plots are stored.
It is called `gerschgorin_plots`. The resolution of the plots in this directory should be better than the preview in some code editors/IDEs.

The directory is in the same `Python working directory` as the script you are running the function in.

```
g.plot(eigenvalues=True, legend=True, save_plot=True)
```

### Example for 3x3 Matrix with complex numbers

```
from gerschgorin_circles import matrix, gerschgorin

# create Matrix
m = matrix.Matrix(
    data = [
        [complex("1+1j"), complex("0-1j"), complex("0-0j")],
        [complex("-5-2j"), complex("0-0j"), complex("0-0j")],
        [complex("1-0j"), complex("0-0j"), complex("-1-1j")]
    ]  
)

g = gerschgorin.GerschgorinCircle(g)
g.plot(eigenvalues=True, legend=True)
```

Output:

![Gerschgorin Circles 2](./gerschgorin_plots/plot_%0A%5B%5B%201.+1.j%20%200.-1.j%20%200.-0.j%5D%0A%20%5B-5.-2.j%20%200.-0.j%20%200.-0.j%5D%0A%20%5B%201.-0.j%20%200.-0.j%20-1.-1.j%5D%5D.svg)

In this example the center of the blue Gerschgorin Circle and an Eigenvalue lie on the same point creating the image of 
a box near (0,0).

## Calculating Circles, Eigenvalues and -vectors

The Gerschgorin Circles are calculated inside the `gerschgorin.plot()` method.
For now, you need to call `gerschgorin.plot(legend=True)` to see the circles in the legend, e.g. `S(1, 5)` 
where the first argument `1+0j` is the coordinate of the circle center and `5` the radius of the circle.
For everything else, including Eigenvalues, -vectors and optionally also determinants see [Other Functionalities](#other-functionalities) 



## Other Functionalities

The `matrix` datastructure is build on top of the numpy `array` implementation
and supports the following operations:

- `__add__` or `+`: Matrix addition
- `__sub__`or `-`: Matrix subtraction
- `__mul__` or `*`: Matrix multiplication
- `matrix.det()`: Calculates determinant of `matrix`
- `matrix.eig()`: Calculates Eigenvalues and Eigenvectors of `matrix`

## Asterisks

- When calling `det()` numpy sometimes throws a `RuntimeWarning`. 
During my testing this did not compromise the results