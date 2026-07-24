'''Rain'''

def main():
    '''Rain'''
    weather = str(input())
    wind_speed = str(input())

    if weather == "Gloomy" and wind_speed == "High" or "Medium":
        print("100%")
    elif weather == "Cloudy" and wind_speed == "Medium":
        print("50%")
    



    if weather == "Clear" and wind_speed == "Low":
        print("0%")
    elif weather == "Gloomy" and wind_speed == "High" or "Medium":
        print("100%")
    elif weather == "Cloudy" and wind_speed == "Medium":
        print("50%")
    else:
        print("Not sure.")

main()
