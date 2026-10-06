class Car():
    def __init__(self):
        self.tyres = []
    def get_tyre(self, position):
        for tyre in self.tyres:
            if tyre.postion == position:
                return tyre 
    def get_all_tyre_info(self):
        for tyre in self.tyres:
            print(f"Tyre position:{tyre.position}, Latest tyre reading: {tyre.readings[-1].reading_text}, Latest tyre reading date: {tyre.readings[-1].date}")


class Tyre():
    def __init__(self, tyre_pressure, tyre_depth, position):
        self.tyre_pressure = tyre_pressure
        self.tyre_depth = tyre_depth
        self.position = position
        self.readings = []

    

class Reading():
    def __init__(self, date, reading_text):
        self.date = date
        self.reading_text = reading_text


car = Car()
fl_tyre = Tyre(5,5,'fl')
fr_tyre = Tyre(5,5,'fr')
bl_tyre = Tyre(5,5,'bl')
br_tyre = Tyre(5,5,'br')

car.tyres = car.tyres + [fl_tyre, fr_tyre, br_tyre, bl_tyre]

reading = Reading(2015, "My reading")

fl_tyre.readings.append(reading)
fr_tyre.readings.append(reading)
bl_tyre.readings.append(reading)
br_tyre.readings.append(reading)

car.get_all_tyre_info()