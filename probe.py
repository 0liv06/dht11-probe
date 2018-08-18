from concretefactory.temperatureSensorFactory import TemperatureSensorFactory
if __name__ == '__main__':
    dht11 = TemperatureSensorFactory.createSensor("DHT11Temperature")
    dht11.changeSetup(21)
    print("Temperature in Celsius: " + dht11.getTemperature() + u"\u00b0" + "C")
    print("Temperature in Fahrenheit: " + dht11.getTemperatureInFahrenheit() + "F")
    print("Temperature in Kelvin: " + dht11.getTemperatureInKelvin() + "K")
