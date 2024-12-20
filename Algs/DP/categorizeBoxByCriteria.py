def categorizeBox(length, width, height, mass):
    """
    :type length: int
    :type width: int
    :type height: int
    :type mass: int
    :rtype: str
    """

    refDim = 10**4
    refVol = 10**9

    refMass = 100

    vol = length * width * height

    bulky = (length >= refDim) or (width >= refDim) or (height >= refDim) or (vol >= refVol)
    heavy = (mass >= refMass)

    if bulky and heavy:
        return "Both"

    elif bulky:
        return "Bulky"

    elif heavy:
        return "Heavy"

    elif not(bulky and heavy):
        return "Neither"

    elif bulky and not(heavy):
        return "Bulky"

    elif not(bulky) and heavy:
        return "Heavy"


res = categorizeBox(1000, 35, 700, 300)

print(res)