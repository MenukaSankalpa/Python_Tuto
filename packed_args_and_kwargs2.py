def my_form(name , height, city):
    print(name, height, city)
    
args = {
    "name": "Menu",
    "height": 21,
    "city": "Kalutara"
}
my_form(**args)    