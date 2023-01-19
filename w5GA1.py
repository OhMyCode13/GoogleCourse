# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    return_city = City()
    if city1.population >= min_population:
        return_city = city1
    if city2.population >= min_population:
        if return_city.name:
            if return_city.elevation <= city2.elevation:
                return_city = city2
        else:
            return_city = city2
    if city3.population >= min_population:
        if return_city.name:
            if return_city.elevation <= city3.elevation:
                return_city = city3
        else:
            return_city = city3
    if return_city.name:
        return return_city.name, return_city.country
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""
