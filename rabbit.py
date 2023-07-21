import webbrowser

print("""\

Wake up...
Follow the white rabbit.

https://github.com/retr080s
                                               

""")

while True:
  
  print("1) Maps/Address search")
  print("2) Username Search")
  print("3) Name Search")
  print("4) Quit")
  
  choice = input("Enter Choice: ")
  
  #choice = choice.strip()
   
  if (choice == "1"):
    print("Enter the address: ")
    address = input()
    urlone = "https://www.google.com/maps/place/" + address
    urltwo = "https://duckduckgo.com/?va=v&t=ha&q=" + address + "&ia=web&iaxm=about&iax=images"
    urlthree = "https://www.openstreetmap.org/search?query=" + address
    webbrowser.open(urlone)
    webbrowser.open(urltwo)
    webbrowser.open(urlthree)
  elif (choice == "2"):
    print("2")
  elif (choice == "3"):
    print("3")
  elif (choice == "4"):
    break
  else:
    print("Invalid Option. Please Try Again.")