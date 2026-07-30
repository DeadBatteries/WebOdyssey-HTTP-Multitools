from Utils.selectOptions import select_number
from Core.Requests.components.Headers.showHeaders import showHeaders
from Core.Requests.components.Cookies.showCookies import showCookies

def requestOptions(item):

    while True:

        print(f"""
{"="*60}
    Request Options:
          
    1-Show Headers
    2-Show Cookies
    0-Back   
{"="*60}  
""")
 
        choice = select_number()

        match choice:

            case 1:
                
                showHeaders(item)
                break

            case 2:

                showCookies(item)
                break

            case 0:
                
                break

