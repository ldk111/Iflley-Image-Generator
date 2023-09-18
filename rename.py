import os 
import main

for route in main.ROUTES:
    try:
        file_old = f".assets/img/test/{main.clean_file_name(route)+'_test'}.png"
        file_new = f".assets/img/test/{main.clean_file_name(route)}.png"
        os.rename(file_old, file_new)
    except:
        print("Test file not found for: " + main.clean_file_name(route))
    