from . import PlotCalculator


def priceByArea(amountPsqft: float, Area: float):
    """This will calculate Plot Price

    Args:
        amountPsqft (float): Amount per square feet
        Area (float): Area of the Plot
    """

    return amountPsqft * Area


def priceBySides(amountPsqft: float, Length: float, Breath: float):

    area = PlotCalculator.area(Length, Breath)

    return area * amountPsqft
