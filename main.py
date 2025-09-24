from app.core.sort import sort


def main():
    """
    Simple interface to test the package sorting function.
    Users can input package dimensions and mass to get the classification result.
    """
    print("=== Package Sorting Interface ===")
    print("Enter package dimensions and mass to classify your package.")
    print("Categories: STANDARD, SPECIAL, or REJECTED")
    print()

    while True:
        try:
            print("Enter package dimensions and mass:")
            width = float(input("Width (cm): "))
            height = float(input("Height (cm): "))
            length = float(input("Length (cm): "))
            mass = float(input("Mass (kg): "))

            result = sort(width, height, length, mass)

            print(f"\nPackage Classification: {result}")
            print()

            volume = width * height * length
            print(f"Package details:")
            print(f"  Volume: {volume:,.0f} cm³")
            print(f"  Max dimension: {max(width, height, length)} cm")
            print(f"  Mass: {mass} kg")
            print()

            again = input("Would you like to classify another package? (y/n): "
                          ).lower().strip()
            if again not in ['y', 'yes']:
                print("Thank you for using the Package Sorting Interface!")
                break
            print()

        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter valid numbers for all dimensions and mass.")
            print()
        except TypeError as e:
            print(f"Error: {e}")
            print("Please enter valid numbers for all dimensions and mass.")
            print()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
