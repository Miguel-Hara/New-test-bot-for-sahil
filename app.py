
# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! from flask import Flask

# Initialize the Flask application

app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    # Return a block of ASCII art text when the root URL is accessed
    return """
███╗░░░███╗██╗░██████╗░██╗░░░██╗███████╗██╗░░░░░  ░█████╗░██╗██╗░░██╗░█████╗░██████╗░░█████╗░
████╗░████║██║██╔════╝░██║░░░██║██╔════╝██║░░░░░  ██╔══██╗╚█║██║░░██║██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║██║██║░░██╗░██║░░░██║█████╗░░██║░░░░░  ██║░░██║░╚╝███████║███████║██████╔╝███████║
██║╚██╔╝██║██║██║░░╚██╗██║░░░██║██╔══╝░░██║░░░░░  ██║░░██║░░░██╔══██║██╔══██║██╔══██╗██╔══██║
██║░╚═╝░██║██║╚██████╔╝╚██████╔╝███████╗███████╗  ╚█████╔╝░░░██║░░██║██║░░██║██║░░██║██║░░██║
╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚═════╝░╚══════╝╚══════╝  ░╚════╝░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝"""

# Run the application
if __name__ == "__main__":
    # Set the host to '0.0.0.0' to make the server publicly available
    # Set the port to 8080
    app.run(host='0.0.0.0', port=8080)

# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! 
