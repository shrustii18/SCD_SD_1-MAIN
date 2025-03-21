def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
  """Converts Celsius to Kelvin."""
  return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
  """Converts Fahrenheit to Kelvin."""
  return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
  """Converts Kelvin to Celsius."""
  return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
  """Converts Kelvin to Fahrenheit."""
  return (kelvin - 273.15) * 9/5 + 32

def main():
  """Main function to handle user input and output."""

  while True:
    print("\nTemperature Conversion Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("7. Quit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
      print("Exiting program.")
      break

    if choice in ('1', '2', '3', '4', '5', '6'):
      try:
        temp = float(input("Enter the temperature value: "))
      except ValueError:
        print("Invalid input. Please enter a number.")
        continue

      if choice == '1':
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {result}°F")
      elif choice == '2':
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C is equal to {result} K")
      elif choice == '3':
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is equal to {result}°C")
      elif choice == '4':
        result = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is equal to {result} K")
      elif choice == '5':
        result = kelvin_to_celsius(temp)
        print(f"{temp} K is equal to {result}°C")
      elif choice == '6':
        result = kelvin_to_fahrenheit(temp)
        print(f"{temp} K is equal to {result}°F")
    else:
      print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
  main()
