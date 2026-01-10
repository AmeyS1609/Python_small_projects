class Planet():
    def __init__(self,name,planet_type,star):
        self.name=name
        self.planet_type=planet_type
        self.star=star
        if not ((isinstance(self.name,str)) and (isinstance(self.planet_type,str)) and (isinstance(self.star,str))):
            raise TypeError("name, planet type, and star must be strings")
            return
        if not ((self.name) and (self.planet_type) and (self.star)):
            raise ValueError("name, planet_type, and star must be non-empty strings")
            return
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    def __str__ (self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"
planet_1=Planet("Earth","Terrestrial Planets ","Sun")
planet_2=Planet("Mars","Terrestrial Planets","Sun")
planet_3=Planet("Jupiter","Gas Giants","Sun")
print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())