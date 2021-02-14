<img src="/static/images/testing.PNG">

## Issues Arising During Testing Cycles

1. Edit review form - this was not initially posting any data to mongo upon submit, but I worked out, somehow, that the reason 
was because the select elements were marked as disabled but contained no value (unlike the input elements), so if you didn't 
make an edit to both of these ratings then the form would not submit as they were blanks. I worked this out through some lengthly 
trial and error testing, and removing the disabled attribute corrected this.

2. Log Out/ Log In issue - sometimes an account will be logged in and able to add reviews, but the nav bar will show the log in
button, despite what the Jinja templating dictates. I've tested this by adding a review when the log in message is showing, and 
the review successfully displays the session.user as a author. Amazingly the solution to this came down to a typo in the script.js 
file! The mouseleave function for the log out button was still labelled as 'Log In' from when I'd copied it, so it would always
display correctly initially, but once hovered over, would display incorrectly.

3. One of the first features I added was an Edit Profile feature, however I forgot that simply using PyMongo's updating command 
will result in overwriting the entire document, so I lost access to a few early test accounts. I tried using some of Werkzeug's
functions to try retrieving an unhashing a password, editing it, then re-hashing and submitting, but to no avail. I compromised 
by writing the $set parameter into the original app route, but leaving out the password altogether. This is obviously something
that will have to be rectified in future releases.

4. The admin-only User page was displaying to all users, then disappeared once a non-admin user logged-in. This was
fixed quickly with a Jinja loop specifying this links to display only if the user was an admin. I have also added an additional
check to all admin pages within the app routes.

5. Admin deleting reviews - After my first mentor review meeting it became clear that quite a lot of my app routes were
redirecting to generic pages rather than back to where a user would expect. For instead upon deleting a review of a particular
pub, the admin would be sent back to the pub index. I put in a lot of time to clearing up these routes, mainly by calling a second
or third collection from MongoDB in order to pass ObjectIds to a redirect request. The result of this is a far better user
experience, and on a personal level this has allowed me to become much more comfortable using Flask and Jinja.

6. The initial draft of this project had a drop-down field for each user to select the drink they purchased during the visit.
I couldn't find an easy way allowing users to add a new drink into the database, and sticking with just the few that I had added 
in meant potentially constraining user reviews. After discussions with my mentor I removed the feature for now.

7. Icons on my various edit and submission forms were not centre-aligning on select items specifically. This was I had erroneously
enclosing my entire form within the div.row element and tag combination, which contained Materialize's 'center' tag. I made various 
attempts at overriding this in DOM child elements, before realising I simply needed to moving the closing div tag to before the 
div.container element that the form was inside. Since I did this on the very first form I made, it meant I had to go and amend all
of them, plus re-indenting all of the code!

8. My mentor challenged me to work out how to restrict review dates being submitted for dates in the past, rather than using the 
generic yearRange option in Materialize's [datepicker](https://materializecss.com/pickers.html). Luckily a handy little codepen by 
[Dakila Lozano](https://codepen.io/dakila/pen/GxbxGB) demonstrated how to manipulate the maxDate range, and a quick check of 
[W3Schools](https://www.w3schools.com/js/js_date_methods.asp) allowed for a quick resolution.

9. Had some whitespace showing underneath the footer because of the Materialize row tag that I'd used inside it, so I moved this 
up to the footer tag and it resolved the issue.

10. On mobile view any buttons I used within a pub or review card are supposed to change from text to an icon view, Because I 
initially used an id property identify them, jQuery was only changing the first item returned from the database. I amended the items
inside the Jinja loop to use a class property instead and all returned items changed.

11. My mentor identified some form submission issues, namely validation of what can be submitted, the minimum values for the price
field and what is a mandatory submission. Most of these can be found just by selected extra parameters on HTML elements, but where I
needed to use regular expressions I used [RegExOne](https://regexone.com/lesson/repeating_characters).

12. Confirmation notices for all delete buttons - I added these by using Materialize's modal to show a confirmation message, and moving
the app route href inside that, quite an easy fix compared to some of the others!

13. My mentor challenged me with handling errors properly, and with the help of a 
[Pythonise tutorial](https://pythonise.com/series/learning-flask/flask-error-handling) I was able to sort this in a matter of minutes.


## Outstanding Issues

1. As mentioned in point #3 above, users cannot currently edit their profile and this is my number one priority to fix as
soon as I understand Werkzeug more.

2. I attempted to come up with a regular expression to control the input of review submissions. I switched the textarea 
element to an input and had a good few hours testing but could come up with nothing that would sufficiently achieve my goal.


## User Stories

As a user I want to...

  1. ... read about a pub I have not visited before.
   - All users, with or without an account, can read all reviews by navigating to the Pubs link in the navigation menu and 
   scrolling or searching for their desired location.

  2. ... rate a pub that I have just visited.
   - Account holders can review a pub by searching for it in the Pubs page. If the pub is returned, they can click into it 
   using the book icon and from there selecting the Add review underneath the pub's information. 
   form that is pre-filled with the pub's name.

  3. ... add a pub that is not yet on the site.
   - If the pub is not present, the user can click the pen icon in the Add a New Pub card. Upon completion of this form, 
   users will be directed to a review form that is pre-filled with the pub's name.

  4. ... find pubs in a city I am visiting.
   - All users, with or without an account, can use the Search box on the Pubs page to filter pubs by name, city or
   country. Clicking on the book icon will take users to a list of reviews of that pub.

  5. ... see my review history.
   - Account holders can view their review history by navigating to the My Profile link on the navigation menu. Reviews are 
   displayed in descending date order.

  5. ... edit a review I previously wrote.
   - Account holders can amend their reviews by navigating to the My Profile link on the navigation menu. Click on the Edit
   button (the pencil icon on mobile devices) to view a pre-filled form which can be edited and submitted.

  6. ... edit my profile information.
   - Account holders can amend their reviews by navigating to the My Profile link on the navigation menu. Underneath the 
   heading is an Edit Profile link in which the user can edit their e-mail address and name. A feature to edit passwords is
   currently in development.

As an administrator, I want to...

  1. ... delete or moderate an offensive review.
   - Administrators can quickly remove or amend any inappropriate or offensive reviews by navigating to the Pub link on the 
   navigation menu. Select or search the relevant pub and the admin will see an additional panel beneath each review. The 
   first button allows the administrator to edit any part of the review except the username of the original author, while the
   delete button can be used where deemed necessary.

  2. ... view a user's review history.
   - As well as viewing all reviews by pub, administrators can also see all reviews by author. Simply navigate to the Users 
   link on the navigation menu to return a list of all active site users. Click on the Moderate button (book icon on mobile 
   devices) to access each user's entire history, and each review will contain an admin panel with choice to edit or delete
   that review as above. Any deletion will need to be confirmed via a prompt message.

  3. ... edit or delete a pub.
   - Deleting false locations can be completed using the regular Pubs link in the navigation menu. On opening, each pub will
   have an additional administrator's panel at the bottom of it's card. The Edit (pencil icon on mobile devices) icon allows
   for the addition or editing of all information, while the delete button (trash can on mobile devices) allows an entry to 
   be removed altogether. Any deletion will need to be confirmed via a prompt message.

  4. ... delete a malicious user.
   - Deleting a persistent offender is as simple as navigating to the User link on the navigation menu. This returns a list
   of all active accounts, and the red Delete (trash can icon on mobile devices) button allows a user to have their access 
   revoke. Any deletion will need to be confirmed via a prompt message.


## Validation

CSS Validator, HTML Validator, JSHint, Flake 8 for Python

### (PEP8 Compliance](http://pep8online.com/)

<img src="/planning/certs/pep8-compliance.PNG">