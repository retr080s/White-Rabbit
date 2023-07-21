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
  print("5) - Plane/Ship Tracker")
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
    print("[+] http://www.findpdfdoc.com/")
  elif (choice == "4"):
    print("Finding information about cryptocurrencies and crypto wallets: ")
    print("[+] https://addresswatcher.com/")
    print("[+] https://www.walletexplorer.com/")
    print("[+] https://oxt.me/")
    print("[+] https://www.fsma.be/en/warnings/companies-operating-unlawfully-in-belgium?field_type_of_fraude_tid_i18n=10595&submit=Apply")
    print("[+] http://bitcoinwhoswho.com/")
    print("[+] https://blockchain.info/")
    print("[+] http://bitcoinwhoswho.com/")
    print("[+] https://www.aware-online.com/en/osint-tools/cryptocurrency-tools/")
  elif (choice == "99"):
    break
  else:
    print("Invalid Option. Please Try Again.")