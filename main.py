import turtle
import pandas

map = 0
print("Wich map do you want to learn?")
while map < 1 or map > 3:
    map = int(input("1. Europe map \n2. Asia\n3. USA \nChoose a map between 1 and 3: "))
    if map < 1 or map > 3:
        print("The number you selected is out of scope. Please try again.")

# Minus 1 because I am using a list
map -= 1
#By Selecting a map i'm going to select a different path: different map,  different csv file, differents countries to learn
country_maps = ["europe_map", "asia_map", "usa_map"]

screen = turtle.Screen()
screen.title(country_maps[map].upper())

screen.addshape(f"./maps/{country_maps[map]}.gif") # It's going to add the shape of the image
turtle.shape(f"./maps/{country_maps[map]}.gif") # It will show the image gif on the screen

data = pandas.read_csv(f"./files/{country_maps[map]}.csv")

all_countries = data.countries.to_list() #Convertion data["countries"] into a list



guessed_countries = []

# The loop will continue until I got all the answers
while len(guessed_countries) < len(all_countries):
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/{len(all_countries)} answers", prompt="What's another country? ").title() # The title will convert the answer into a capital

    if answer_country == "Exit": # leave the loop

        missing_countries = [country for country in all_countries if country not in guessed_countries] # Using Dictionary comprehension
        new_data = pandas.DataFrame(missing_countries)

        #Creatingg a csv file for each country with the countries to learn
        new_data.to_csv(f"./files/{country_maps[map]}_to_learn.csv")  # It will create a new .csv file with that name
        break




    #Using a turtle to write the answer on the map only if not already guessed
    if answer_country in all_countries and answer_country not in guessed_countries:
        guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = data[data.countries == answer_country]
        t.goto(int(answer_data.x), int(answer_data.y)) # because is a row that we can use the columns too, this coordenates are str too so must be converted into int
        t.write(answer_country) #it will write the country_name of the coordenates registered, if i put country_data it will give more information from the csv


screen.exitonclick()