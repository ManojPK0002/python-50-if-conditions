'''Smart Home Automation:
Develop a program for a smart home system.
Use nested if statements to simulate the automation of lights, temperature,
and security based on user preferences and environmental conditions.
'''


# User required
lights_on = True
desired_temperature = 22
security_enabled = True

# Environmental Conditions
ambient_light = "bright"
ambient_temperature = 25
intruder_detected = False

if ambient_light == "bright":
    lights_on = False
elif ambient_light == "dim":
    lights_on = True

if ambient_temperature > desired_temperature:
    print("It's too hot. Turning on air conditioning.")
elif ambient_temperature < desired_temperature:
    print("It's too cold. Turning on heater.")


if security_enabled and intruder_detected:
    print("Intruder detected! Alerting authorities.")
elif security_enabled:
    print("No intruder detected. Security system active.")

print("\nCurrent Status:")
print(f"Lights are {'on' if lights_on else 'off'}")
print(f"Desired Temperature: {desired_temperature}°C")
print(f"Security System: {'enabled' if security_enabled else 'disabled'}")
