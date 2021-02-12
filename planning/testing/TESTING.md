<img src="static/images/testing.PNG">

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

11. My mentor identified some form submission issues, namely validation of what can be submitted and what is a mandatory submission

## Outstanding Issues

1. The Materialize datepicker currently allows for a user to publish a review on a date in the future. While their 
[documentation](https://materializecss.com/pickers.html) allows for the setting of a maximum date, I couldn't find a way to 
successfully retrieve the current date and set that as the maximum.

## User Stories



## Validation

CSS Validator, HTML Validator, JSHint, Flake 8 for Python