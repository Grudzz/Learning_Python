import webbrowser


print("Choose 1 for stock websites")

print("Choose 2 for shoping websites")

user_input = int(input())

def launch_website(user_input):
    if user_input == 1:
        webbrowser.open("https://robinhood.com/us/en/")
        webbrowser.open("https://www.marketwatch.com/")
    if user_input == 2:
        webbrowser.open("https://www.newegg.com/")
        webbrowser.open("https://www.amazon.com/")

        
launch_website(user_input)
