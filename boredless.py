destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', 'historical site', 'art']

def get_destination_index(destination):
  get_destination_index = destinations.index(destination)
  return get_destination_index


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index (traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)


attractions = [[] for list in destinations]

# [ [], [],]

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions[destination_index].append(attraction) 
  attractions_for_destination = attractions[destination_index]
  return (attractions_for_destination)

add_attraction('Los Angeles, USA',['Venice Beach', ['beach']])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Paris, France", ["Torre Eiffle", ["monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


def find_attractions(destination: str, interests: list[str]):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for possible_attraction in attractions_in_city:
    # ["Pyramids of Giza", ["monument", "historical site"]])
    for interest in interests: 
      interests_of_attraction = possible_attraction[1]
      if interest in interests_of_attraction:
        attractions_with_interest.append(possible_attraction)
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
   
  for index, item in enumerate(traveler_attractions):
    if index > 0:
      interests_string += ", " + item[0]
    else:
      interests_string += item[0]
  interests_string += "."
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
