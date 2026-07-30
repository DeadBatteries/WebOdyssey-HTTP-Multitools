def showCookies(item):

    c = item["cookies"]

    print("="*80)   
    print("Cookies")    
    print("="*80)
     
    for key, value in c.items():
    
        print(f"{key:<25}:{value}")

