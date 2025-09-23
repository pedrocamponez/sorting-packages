def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    This function sorts packages based on their dimensions and mass, classifying them into one of the following categories:

    - A package is "bulky" if its volume (Width * Height * Length) is greater than or equal 1,000,000 cubic centimeters OR when one of its dimensions is greater or equal to 150 centimeters.
    - A package is "heavy" if its mass is greater than or equal to 20 kg.

    The packages must be dispatched in the following:
    - "STANDARD" means the package is neither "BULKY" nor "HEAVY"
    - "SPECIAL" means the package is either "BULKY" or "HEAVY"
    - "REJECTED" means the package is both "BULKY" and "HEAVY"

    All inputs must be numbers.

    The function returns a string.
    """
    if (width * height * length >= 1000000) or (width >= 150) or (height >= 150) or (length >= 150):
        print("bulky")
        if mass >= 20:
            print("bulky AND heavy")
            return "REJECTED"
        else:
            print("bulky AND light")
            return "SPECIAL"
    else:
        print("not bulky, not rejected")
        if mass >= 20:
            print("heavy")
            return "SPECIAL"
        else:
            print("not bulky, not heavy")
            return "STANDARD"
