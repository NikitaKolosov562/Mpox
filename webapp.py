from flask import Flask, url_for, render_template,request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


    
@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    artist = request.args['artist']
    artist2 = request.args['artist2']    
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    
    reply1 = "error"
    if artist == 'Taylor Swift':
        reply1 = "You should you listen to Bad Blood by Taylor Swift!"
    
   
    if artist == 'The Weeknd':
        reply1 = "You should you listen to Blinding lights by The Weeknd!"
    
  
    if artist == 'Travis Scott':
        reply1 = "You should you listen to Goosebumps by Travis Scott!"
    
    
    
    reply2 = "error"
    if artist2 == 'Osamason':
        reply2 = "You should you listen to I know what you did last Summer by Osamason!"
    
   
    if artist2 == 'Nettspend':
        reply2 = "You should you listen to We not like you by Nettspend!"
    
  
    if artist2 == 'Baby Kia':
        reply2 = "You should you listen to OD Crashin by Baby Kia!"
    return render_template('response.html', response1 = reply1, response2 = reply2)
    

@app.route("/p1")
def render_page1():
    return render_template('page1.html')


    
if __name__=="__main__":
    app.run(debug=True)
