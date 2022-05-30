from flask import *
import webbrowser
import threading
import random



#defines the websitePage
app = Flask(__name__)

#browser module, simply opens it on the browser
def openBrowser():
    webbrowser.open("http://127.0.0.1:5000/")

#runs the website once executed
#simply running it will create a local link that stays the same
#http://127.0.0.1:5000/ 
def runWebsite():
    app.run()

    #app.run(host='0.0.0.0', port=81)
    #other option /\

#a line is to create the main frontpage
@app.route('/')
def test():
    testvar = str(random.randint(1, 100))
    #heres something you cannot do in a normal HTML file
    return("<h1>this " + testvar + """ a test</h1>

<other href="/another">the other</other>""")#hyperlink to the other page
    
#add an app.route(Link) to create another page
@app.route('/another')
#the next function will be the next page made.
def another():
    return("another website")

#i made a thread so it works in the back of the pc
#otherwise it will not allow the code to do more than host this site.
createInstance = threading.Thread(target = runWebsite)
createInstance.start()

#opens it for you :D
openBrowser()
