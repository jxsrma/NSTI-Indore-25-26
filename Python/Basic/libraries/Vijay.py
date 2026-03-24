from Builder import PlotCalculator, PriceCalculator

area = PlotCalculator.area(40, 50)
print('Area:', area)
print('Meter to Feet', PlotCalculator.meterToFeet(10))
print('Meter to Feet', PlotCalculator.feetToMeter(10))


print('Amount of Plot', PriceCalculator.priceByArea(5000, area))

print(PriceCalculator.priceBySides(4000, 40, 50))
