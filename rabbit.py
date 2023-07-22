print("""\

Wake up...
Follow the white rabbit.

https://github.com/retr080s
                                               

""")

while True:
  
  print("1) - Archived Web Pages")
  print("2) - Dark Web")
  print("3) - Documents")
  print("4) - Crypto Wallet Tracker")
  print("5) - Ship, Yacht, Boat, Plane, Helicopter Live Tracker")
  print("6) - Image Search")
  print("7) - Cameras (Live Feed)")
  print("8) - Maps")
  print("99) - Exit")
  
  choice = input("Enter Choice: ")
  
  #choice = choice.strip()
   
  if (choice == "1"):
    print("Here are some links that might help you: ")
    print("[+] https://archive.is")
    print("[+] https://archive.org")
    print("[+] https://github.com/hartator/wayback-machine-downloader")
    print("[+] https://www.aware-online.com/osint-tools/web-archive-search-tool/")
    print("[+] https://cachedview.com/")
    print("[+] https://www.cachedpages.com/")
  elif (choice == "2"):
    print("Dark web search engines: ")
    print("[+] https://tor.taxi/")
    print("[+] https://ahmia.fi/")
    print("[+] https://darkwebnews.com/")
    print("[+] https://www.deepweb-sites.com/deep-web-search-engines/")
    print("[+] https://www.torscan.io/")
    print("[+] https://onions.es/")
  elif (choice == "3"):
    print("Search engine used for finding documents: ")
    print("[+] https://www.findpdfdoc.com/")
  elif (choice == "4"):
    print("Finding information about cryptocurrencies and crypto wallets: ")
    print("[+] https://addresswatcher.com/")
    print("[+] https://www.walletexplorer.com/")
    print("[+] https://oxt.me/")
    print("[+] https://etherscan.io/")
    print("[+] https://bitcoinwhoswho.com/")
    print("[+] https://blockchain.info/")
    print("[+] http://bitcoinwhoswho.com/")
    print("[+] https://www.aware-online.com/en/osint-tools/cryptocurrency-tools/")
  elif (choice == "5"):
    print("Tracker for yachts, boats, ships, planes and helicopters: ")  
    print("[+] https://www.marinetraffic.com")
    print("[+] https://www.myshiptracking.com/")
    print("[+] https://www.marinevesseltraffic.com/")
    print("[+] https://shiptracker.live/")
    print("[+] https://www.flightradar24.com")
    print("[+] https://www.radarbox.com")
    print("[+] https://planefinder.net/")
  elif (choice == "6"):
    print("Image/Video search engines: ")
    print("[+] https://yandex.com/images/")
    print("[+] https://www.bing.com/?scope=images&nr=1&FORM=NOFORM")
    print("[+] https://image.baidu.com/")
    print("[+] http://fotoforensics.com/")
    print("[+] https://www.google.com/imghp")
    print("[+] https://findface.ru/")
    print("[+] https://www.imageidentify.com/")
    print("[+] https://imgops.com/")
    print("[+] https://pimeyes.com/en")
    print("[+] https://rootabout.com/")
    print("[+] https://www.reverse-image-search.org/")
  elif (choice == "7"):
    print("Links to the cameras with live feed and unsecured cameras: ")
    print("[+] https://reolink.com/unsecured-ip-camera-list/")
    print("[+] https://www.123webcam.com/")
    print("[+] https://airportwebcams.net/")
    print("[+] https://www.earthcam.com/")
    print("[+] https://www.insecam.org/")
    print("[+] https://worldcam.eu/")
   elif (choice == "8"):
    print("World maps + Social media maps ")
    print("[+] https://dualmaps.com/")
    print("[+] https://livingatlas.arcgis.com/wayback")
    print("[+] https://www.mapchecking.com/")
    print("[+] https://zoom.earth/")
    print("[+] https://www.bing.com/maps")
    print("[+] https://www.maxar.com/")
    print("[+] https://usa.liveuamap.com/")
    print("[+] https://www.instantstreetview.com/")
    print("[+] https://umap.openstreetmap.fr/en/map/islamic-state-claimed-provinces-map_29647#7/34.012/44.846")
    print("[+] https://www.google.com/maps/")
    print("[+] https://yandex.com/maps/")
    print("[+] https://www.strava.com/heatmap")
    print("[+] https://map.snapchat.com/")
    print("[+] https://www.openseamap.org")
  elif (choice == "99"):
    break
  else:
    print("Invalid Option. Please Try Again.")