import main

#for route in main.ROUTES:
#    main.highlight_route(route, save=True)

#REGENERATE LUFTWAFFE
#Foot Up!
#Shelve It
#Half Pebble Slab
#The Bat
#Dyno 8
#main.highlight_route("Luftwaffe", regenerate=True, save=True)
#main.highlight_route("Foot Up!", regenerate=True, save=True)
#main.highlight_route("Shelve It", regenerate=True, save=True)
#main.highlight_route("Half Pebble Slab", regenerate=True, save=True)
#main.highlight_route("The Bat", regenerate=True, save=True)
#main.highlight_route("Dyno 8", regenerate=True, save=True)

main.cache_routes(regenerate = False, remove_background=True, suffix="_test")

for route in main.ROUTES:
    print("Compressing route " + route)
    main.compress_route(route, suffix="_test")