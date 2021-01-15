<img src="static/images/text-logo.PNG">

Welcome to my interactive front-end development milestone project. For this project I chose to create 
[pintbaby](https://www.pintbaby.herokuapp.com/), a website that allows users to add and review pubs around the world.



## User Experience

### Styling

- A [Balsamiq](https://www.balsamiq.com/) wireframe for this project is included in the repository, with 
[desktop/tablet](planning/wireframes/#.pdf) and [mobile](planning/wireframes/#.pdf) versions.

I used the following hex colours, selecting using [Pixlr](https://www.pixlr.com/):

 - 
 - 
 - 
 - 
 - 

- Fonts - Titillium provided a font that gave me both an upper and lower case view that I liked. Looking at fonts is generally a 
pretty boring task but an important one nonetheless, Titillium provides upper case that allows for the creation of a good logo, 
and a lower case that could be used across the site without looking tired or cliche.
- The icons I used within this project are all sources from [Font Awesome](https://fontawesome.com/)'s free package.

### User Stories

Testing for each of the below user stories is included within the [testing log](TESTING.md).

As a user I want to...

  1. ... find somewhere to stay overnight before the match;
  2. ... find a place to get a drink;
  3. ... find a restaurant to eat in after the match;
  4. ... find a place to get a coffee;
  5. ... find something else to do;
  6. ... find a specific place that I was recommended.
  7. ... recommend a club or league for addition to the site.


## Features

### Existing Features

- The starting point for any user story on AwayDay is the dropdown menu. Selecting any club crest from the following leagues will
display the location of their home stadium:
    - Football/Soccer
        - [English Championship](https://www.efl.com/clubs-and-competitions/sky-bet-championship/);
        - [English Premier League](https://www.premierleague.com/);
        - [German Bundesliga](https://www.bundesliga.com/en/bundesliga);
        - [League of Ireland Premier Division](https://sseairtricityleague.ie/);
    - Gaelic Football and Hurling
        - [Gaelic Athletic Association](https://www.gaa.ie/);
    - Ice Hockey
        - [National Hockey League](https://www.nhl.com/);
    - Rugby League
        - [European Super League](https://superleague.co.uk/);
- The four search refine buttons allow users to the search for pubs, cafes, hotels and restaurants. This returns the top five 
entries based on Google's Prominence ranking.
- The search box allows for a user to find any other type of location beyond the four above, or a particular place using AutoComplete. 
There are issues with this feature that are detailed in the [testing](TESTING.md) log.
- Each place that Google returns is then assigned a clickable marker that displays the place's name, rating and website, as well as 
that location's top-ranked photograph.

### Features to Implement

- Share plans with friends - I signed up to ShareThis during the project with a view to adding some pre-made share buttons to the 
site, but was getting quite a lot of console warnings about non-loadable content, so this feature has been omitted from the 
first release.
- Directions - I'd like to include a feature to generate directions between any given marker and the stadium being visited, or 
vice versa. I briefly explored Google's Directions API but I already had my hands full with the Places API.
- Rollout to more leagues, sports and countries - The only thing I need to achieve this is the latitude and longitude of each 
club's home stadium, and a good quality PNG club crest, so this could be quite easy to implement. My current main priorities are 
NFL, NBA, NRL and AFL.
- A wider league selection would certainly require a re-structure of the drop-down options, the format I've used is already at the 
limit of what it can display well on smaller devices. The most obvious solution would be to group leagues by sport and introduce 
a secondary drop-down layer.
- Fixture API implementation - the holy grail! There's a host of sports data APIs out there, especially for football, and I'd love 
to be able to generate a team's fixtures, then select an opponent that way.
- Itineraries - the ability to store locations would be great for users who are planning far in advance of a trip, while a 'Current 
Location' feature would allow users to bypass the club selection phase, especially if there are multiple dropdowns and they are 
looking for somewhere to go immediately.
- As I got more confident with using JS I've realised how enormous the map.js file is. I wrote all of those consts at the very start
of the project when I was least comfortable with the language, so once I've got my results back I'll be doing some serious 
optimisation on this file just as a personal learning exercise.


## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML is the language used to display and structure information on any website.

- [CSS3](https://en.wikipedia.org/wiki/CSS3)
    - Cascading Style Sheets is the language used to style HTML content.

- [Materialize](https://materializecss.com/)
    - Materialize's grid framework helped me bring my initial wireframe ideas to life.

- [Javascript](https://www.javascript.com/)
    - The language that makes the web interactive.

- [jQuery](https://jquery.com/)
    - An open-source Javascript library that simplifies interactive web design.

- [Font Awesome](https://fontawesome.com/)
    - Font Awesome's free package provides a comprehensive icon suite that is fully customisable in CSS.
    
- [Google Fonts](https://fonts.google.com/)
    - Google's free service provided countless fonts to help your project stand out.

- [Gitpod](https://www.gitpod.io/)
    - A software development editor perfect for personal or collaborative use.

- [GitHub](https://www.github.com/)
    - The world's leading code-hosting platform.

- [Heroku](https://www.heroku.com/)
    - >>>

- [EmailJS](https://www.emailjs.com/)
    - Client-side Javascript software that I used to create the this project's contact form.

- [Balsamiq](https://www.balsamiq.com/)
    - An intuitive drafting tool that enables visual planning at the start of a project.

- [Pixlr](https://www.pixlr.com/)
    - Pixlr is a great free software package that enabled me to quickly pick out hex colors and edit images;

- [Favicon.io](https://favicon.io/)
    - A quick and easy tool to create favicons for display in the address bar.

- [MongoDB](https://www.mongodb.com)
    - A non-relational database >>>


## Testing

I have included a [testing log](TESTING.md) within the repository.

In terms of look and feel, the site is similar across all browsers. The tablet and desktop views are almost identical, while 
mobile devices always drop into col-12 formatting. The mobile and tablet views both place buttons underneath a map that stretches to 
fill the screen width. For mobile devices, I have included Bootstrap's trusty collapsible navbar.

I tested this project primarily on Firefox but also Chrome and Edge, taking advantage of the screen size options to test using iPad, 
Samsung Galaxy and Kindle Fire. I also tested the site on my own Huawei device, as well as passing the initial site on to some friends
for UI feedback.


## Deployment

I used [GitHub](https://www.github.com/) as the host for this project, and [GitPod](https://www.gitpod.io/) to write it, using 
just a single branch. There were a few instances where I had to remove significant amounts of trial-and-error code after hours of 
testing, utilising forking and branching would definitely have helped cut down development time.

I deployed this project to GitHub Pages using the following method:

1. Locate the desired repository in your repository list and open it;
2. Navigate to the Settings heading in the repository heading;
3. Locate the GitHub Pages heading at the bottom of the page;
4. Click the button beneath the Source sub-heading and change this from 'None' to 'Master Branch';
5. Once the page reloads, locate the GitHub Pages heading again;
6. If successful, a green box will appear beneath the heading with the link to your deployed page;
7. This page will only update with new content once that content has been pushed from your developer environment.

### Cloning

Assuming you already have Git [installed](https://git-scm.com/download/), anybody can clone this repository by following these steps:

- Open the command prompt/terminal on your machine;
- Type the command 'cd' followed by the directory you wish to store the repository in;
- Go to the top of the [GitHub repository](https://github.com/kiehozero/away-day/) and click the green 'Code' drop-down button;
- Copy the [link provided](https://github.com/kiehozero/away-day.git);
- Return to the Command Prompt and type 'git clone' followed by the copied address.

For an in-depth guide to cloning repositories, click [here](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/), from 
which the steps above were taken.


## Credits

### Content

- A few of the more advanced JavaScript functions in the [map script](assets/scripts/map.js) were taken from a 
[Google Code Labs tutorial](https://codelabs.developers.google.com/codelabs/google-maps-nearby-search-js/#0) that I dug out from 
their documentation, namely the infoWindow functions.
- I wanted to keep everything on a single HTML page, and providing a contact form via a modal was how I achieved this. Bootstrap's 
[documentation](https://getbootstrap.com/docs/4.0/components/modal/) on this was straightforward and provided a good shell, while the 
jQuery came from [Tutorial Deep](https://tutorialdeep.com/knowhow/open-bootstrap-modal-on-button-click-jquery/).
- I waded into the battlefield that is StackOverflow a few times, often emerging more confused than when I arrived, but 
[this](https://stackoverflow.com/questions/18616040/bootstrap-horizontal-drop-down) thread helped untangle some styling dropdown 
issues. I also took to the ever-reliable [W3 Schools](https://www.w3schools.com/bootstrap4/bootstrap_utilities.asp) tutorials to help 
iron out some margin and padding issues when moving between screen widths. I've definitely learnt in this project that less is often 
more with CSS and Bootstrap.

### Tutorials

- Google's own [tutorials](https://developers.google.com/maps/documentation) give a great run-down of how to get started using maps. 
They aren't too great for showing you how to customise beyond what they have already given, but their documentation and setup guides 
were invaluable.
- Some of the styling and map dos and don'ts from Sitepoint's great 
[tutorial](https://www.sitepoint.com/google-maps-javascript-api-the-right-way/)
- Envato Tut's [YouTube tutorial](https://www.youtube.com/playlist?list=PLgGbWId6zgaXFR4SW_3qJ55cxmEqRNIzx) helped me understand some 
of the coding concepts behind the map.
- jQuery's [documentation](https://api.jquery.com/) has an article on every function in their library it was one of the few parts of 
learning JavaScript that made sense immediately. The [section](https://api.jquery.com/toggleClass/) on class toggling solved 
bug #7 listed in my [testing log](TESTING.md).
- Just when I didn't think anybody couldn't sufficiently simplify the infoWindow process for me, Chris Minnick's 
[Webucator tutorial](https://www.webucator.com/how-to/how-add-an-info-window-google-map.cfm) finally gave me the breakthrough I needed.

### Media

- League and club logos were sourced from the following locations:
    - [English Championship](https://www.efl.com/clubs-and-competitions/sky-bet-championship/);
    - [English Premier League](https://www.premierleague.com/);
    - [German Bundesliga](https://www.bundesliga.com/en/bundesliga);
    - [League of Ireland Premier Division](https://www.sseairtricityleague.ie/);
    - [Gaelic Athletic Association](https://www.gaa.ie/);
    - [National Hockey League](https://www.nhl.com/);
    - [European Super League](https://www.superleague.co.uk/);
    - [Wikipedia](https://en.wikipedia.org/)

### Acknowledgements

- My mentor Precious Ijege recommended adding a search box after my initial presentation. Luckily Google's
 [PlaceBox setup](https://developers.google.com/maps/documentation/javascript/examples/places-searchbox?hl=ja) ensured that I flew 
 through adding this to the project.
- An enormous thank you to Kevin Loughrey, Samantha Dartnall, Cormac Lawlor and Michael Park at Code Institute for helping sort out 
some of the trickier issues when calling the Places API. It is frustrating to have to submit things to tutors knowing you are close 
to a solution, but they saved me hours of experimenting towards a solution with concise explanations.