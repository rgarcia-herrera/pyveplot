from numbers import Number
from math import sqrt

try:
    from numpy import sin, cos, radians
except ImportError:
    from math import sin, cos, radians


import svgwrite


def or_(orig, default):
    """Use ``orig``, unless it is None: then use ``default``"""
    return default if orig is None else orig


class UnitConverter(object):
    """Measurements taken from https://oreillymedia.github.io/Using_SVG/guide/units.html"""

    table = {
        "px": 1,
        "in": 96,
        "cm": 37.795,
        "mm": 3.7795,
        "pt": 1 / 0.75,
        "pc": 16,
        None: 1,
    }

    def __init__(self, width=None, height=None, font_size=None):
        """Class for converting between SVG units"""
        self.table = self.table.copy()
        self.font_size = font_size  # pt
        if self.font_size is not None:
            self.table["em"] = self.table["pt"] * self.font_size
            self.table["en"] = self.table["em"] / 2

        self.width = None if width is None else self.to_px(width)
        self.height = None if height is None else self.to_px(height)

        if self.width is not None:
            self.table["vw"] = self.width / 100

        if self.height is not None:
            self.table["vh"] = self.height / 100
            if self.width is not None:
                self.table["vmin"], self.table["vmax"] = [
                    x / 100 for x in sorted((self.width, self.height))
                ]
                self.table["%"] = (1 / 100) * (
                    sqrt(self.width ** 2 + self.height ** 2) / sqrt(2)
                )

    def to_px(self, val, unit=None):
        """Convert the given value into px. Compatible with numpy.

        If ``val`` is a string with units, these will be used:
        otherwise, the unit can be explicitly passed.

        Parameters
        ----------
        val
        unit

        Returns
        -------
        float
        """
        detected_unit = None
        if isinstance(val, str):
            val, detected_unit = svgwrite.utils.split_coordinate(val)
        if detected_unit is None:
            detected_unit = unit
        return val * self.table[detected_unit]

    def from_px(self, val, unit):
        """Convert the give px value into the requested unit.

        If the passed ``unit`` is None, the px value will be returned as a float.

        If the passed ``val`` is a number (or unitless string),
        a string with units will be returned.

        If the passed ``val`` is a numpy array,
        a numpy array will be returned: there will be no unit strings.

        Parameters
        ----------
        val: float
            px value to convert
        unit: str, optional
            If none, the px value will be returned

        Returns
        -------

        """
        converted = float(val) / self.table[unit]
        if isinstance(val, Number) and unit:
            return str(converted) + unit
        else:
            return converted

    def __call__(self, val, tgt=None, src=None):
        return self.from_px(self.to_px(val, src), tgt)

    def _kwargs(self):
        return {"width": self.width, "height": self.height, "font_size": self.font_size}

    def copy(self, **kwargs):
        """Copy the UnitConverter, changing its init args as given."""
        return type(self)(**dict(self._kwargs(), **kwargs))


class PolarPlotter(object):
    def __init__(self, x=0, y=0, use_radians=True, **kwargs):
        """Class for converting polar coordinates into Cartesian coordinates.

        Parameters
        ----------
        x: float | str
            x location of origin, in any SVG units
        y: float | str
            y location of origin, in any SVG units
        use_radians: bool, optional
            Whether to use radians for angles by default (default True)
        kwargs:
            ``width``, ``height``, ``font_size`` kwargs to pass to internal ``UnitConverter``
        """
        self.converter = UnitConverter(**kwargs)
        self.x = self.converter.to_px(x)
        self.y = self.converter.to_px(y)
        self.use_radians = use_radians

    def __call__(self, distance, angle, use_radians=None):
        """Convert polar coordinates into Cartesian coordinates in px.

        Compatible with numpy arrays.

        Parameters
        ----------
        distance: float | str
            radial distance, in any SVG units
        angle: float
            polar angle from the 12 o'clock position
        use_radians: bool, optional
            Whether to use radians for angles. By default, use the object's default.

        Returns
        -------
        tuple
            x, y coordinates in px/user units from the top left
        """
        if use_radians is None:
            angle = self.use_radians
        if not use_radians:
            angle = radians(angle)

        distance = self.converter.to_px(distance)

        x = self.x + distance * sin(angle)
        # negative because SVG thinks from the top left, not bottom
        y = self.y - distance * cos(angle)
        return x, y
