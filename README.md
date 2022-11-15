# Movie_Lookup_API
Learned working with API, Tkinter, and  to produce data about movies.
<h1> Abstract </h1>
I designed a GUI to look up movies via an API (OMdb). Information regarding any movie can be looked up via title. 
<h2> Introduction </h2>
<p>I was interested in APIs and learning how they operate. I went with the topic of film because I felt like it would have simple functionality and be perfect to learn how the method works. We start by importing the required models (mentioned to the right). Then we create our canvas, I used tkinter as I had previous experience with the model. Then we define a function that would later be used as a command for the search button. Then we set up a command that sends the request to the cloud and catches the requested data. Apply the appropriate names and tag them. Set up an exception that pops an error if there are problems regarding the requesting and receiving of data. Set up a label using tkinter which displays the user-requested data. Then we set up the link button using the webbrowser module that should pop up after a search is made and the button is clicked. Finally, we complete the code by adding a entry and a search button with the command that executes afore mentioned defined function.</p>
<h3> Python Models Used </h3>
<p> The models used were:
tkinter, to design the GUI.
requests, which help in establishing API and receiving/pinging.
json, which helps make the JSON data derived from the API readable.
Webbrowser, which helps create a button embedded with a link to the poster. </p>
<h2> Output </h2>
<p>![GUI](https://user-images.githubusercontent.com/103015857/201828120-27f3d955-5e65-4873-998e-29c885af99ce.png)</p>
<p>![Output](https://user-images.githubusercontent.com/103015857/201828122-a07d66ce-430f-447c-8eb0-0f41f1e44a15.png)</p>
<p>![Poster_PopUP](https://user-images.githubusercontent.com/103015857/201828123-c61ede99-76fd-4158-91bb-983a26a6d533.png)</p>
