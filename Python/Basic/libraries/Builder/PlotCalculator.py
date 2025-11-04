def area(Length: float, Breath: float):
    """This will calculate Plot Area

    Args:
        Length (float): Length of the Plot
        Breath (float): Breath of the Plot
    """

    return Length * Breath


def meterToFeet(Length: float):
    """Convert Meter into Feet

    Args:
        Length (float): Length in meter
    """

    return Length * 3.28084


def feetToMeter(Length: float):
    """Convert Feet into Meter

    Args:
        Length (float): Length in Feet
    """

    return Length / 3.28084


if __name__ == "__main__":
    print("Hello")
