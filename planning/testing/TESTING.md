<img src="/static/images/testing.PNG">

1. Edit review form - this was not initially posting any data to mongo upon submit, but I worked out, somehow, that the reason 
was because the select elements were marked as disabled but contained no value (unlike the input elements), so if you didn't 
make an edit to both of these ratings then the form would not submit as they were blanks. I worked this out through some lengthly 
trial and error testing, and removing the disabled attribute corrected this.

2. Log Out/ Log In issue - sometimes an account will be logged in and able to add reviews, but the nav bar will show the log in
button, despite what the Jinja templating dictates. I've tested this by adding a review when the log in message is showing, and 
the review successfully displays the session.user as a author. Amazingly the solution to this came down to a typo in the script.js 
file! The mouseleave function for the log out button was still labelled as 'Log In' from when I'd copied it, so it would always
display correctly initially, but once hovered over, would display incorrectly.

3. Password editing submissions

4. The admin-only User and Pint pages were displaying to all users, then disappeared once a non-admin user logged-in. This was
fixed quickly with a Jinja loop specifying this links to display only if the user was an admin.

5. Admin deleting reviews - wanted this to redirect to the pub's own page rather than to an index, needed to pass in the pub's 
ID, not resolved this yet, tried deleting the return redirect but got a Jinja error back, the fix I've put in for now is that the
route redirects to the generic pub index page rather than that pub's particular page

6. Mention removal of pints drop-down

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
field and what is a mandatory submission

12. Confirmation notices for all delete buttons, added these by using Materialize's modal to show a confirmation message, and moving
the app route href inside that

## Outstanding Issues

1. Edit password issue
2. 
3. 

## User Stories

As a user I want to...

  1. ... read about a pub I have not visited before.
   - 
  2. ... rate a pub that I have just visited.
   - 
  3. ... find pubs in a city I am visiting.
   - 
  4. ... review a pub that is not yet on the site.
   - 
  5. ... see my review history.
   - 
  6. ... edit or amend a review I previously wrote.
   - 

As an admin, I want to
  1. ... delete or moderate an offensive review.
   - 
  2. ... view a user's review history.
   - 
  3. ... delete a pub.
   - 
  4. ... delete a malicious user.
   - 

## Validation

CSS Validator, HTML Validator, JSHint, Flake 8 for Python