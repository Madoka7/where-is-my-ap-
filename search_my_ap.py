import webbrowser
import sys
import time
#browser = webdriver.Chrome()
i=int(sys.argv[1])
while i<int(sys.argv[2]):
    webbrowser.get('chrome %s').open_new_tab("192.168.0."+str(i))
    i=i+1
    #sleep(1)

