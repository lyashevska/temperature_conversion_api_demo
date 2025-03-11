def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature in Fahrenheit.
    """
    return (celsius * (9 / 5)) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature in Celsius.
    """
    return (fahrenheit - 32) * (5 / 9)


def celsius_to_kelvin(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Kelvin.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature in Kelvin.
    """
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Converts a temperature from Kelvin to Celsius.

    Args:
        kelvin: The temperature in Kelvin.

    Returns:
        The temperature in Celsius.
    """
    return kelvin - 273.15


def check_temperature_validity(temperature: float, unit: str) -> bool:
    """
    Checks if a temperature is valid for a given unit.

    Args:
        temperature: The temperature to check.
        unit: The unit of the temperature. Must be "C", "F", or "K".

    Returns:
        True if the temperature is valid, False otherwise.
    """
    abs_zero = {"C": -273.15, "F": -459.67, "K": 0}
    if temperature < abs_zero[unit]:
        return False
    return True


def check_unit_validity(unit: str) -> bool:
    """
    Checks if a unit is valid.

    Args:
        unit: The unit to check. Must be "C", "F", or "K".

    Returns:
        True if the unit is valid, False otherwise.
    """
    if not unit in ["C", "F", "K"]:
        return False
    return True


def convert_temperature(temperature: float, unit: str) -> tuple:
    """
    Converts a temperature from one unit to another.

    Args:
        temperature: The temperature to convert.
        unit: The unit of the temperature. Must be "C", "F", or "K".

    Returns:
        A tuple containing the converted temperature in Celsius and Kelvin units.

    Raises:
        ValueError: If the unit is not "C", "F", or "K".
        ValueError: If the temperature is below absolute zero for the given unit.

    Examples:
        >>> convert_temperature(32, "F")
        (0.0, 273.15)
        >>> convert_temperature(0, "C")
        (32.0, 273.15)
        >>> convert_temperature(273.15, "K")
        (0.0, -459.67)
    """
    if not check_unit_validity(unit):
        raise ValueError("Invalid unit")
    if not check_temperature_validity(temperature, unit):
        raise ValueError("Invalid temperature")
    if unit == "F":
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = celsius_to_kelvin(celsius)
        return celsius, kelvin
    if unit == "C":
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        return fahrenheit, kelvin
    if unit == "K":
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return celsius, fahrenheit

if __name__ == "__main__":
    print(convert_temperature(0, "C"))
    print(convert_temperature(0, "F"))
    print(convert_temperature(0, "K"))
    print(convert_temperature(-500, "K"))
    print(convert_temperature(-500, "C"))
    print(convert_temperature(-500, "F"))
    print(convert_temperature(-500, "B"))
