<img src="static/images/testing.PNG">

1. Edit review form - this was not initially posting any data to mongo upon submit, but I worked out, somehow, that the reason 
was because the select elements were marked as disabled but contained no value (unlike the input elements), so if you didn't 
make an edit to both of these ratings then the form would not submit as they were blanks. I worked this out through some lengthly 
trial and error testing, and removing the disabled attribute corrected this.

2. Log Out/ Log In issue - sometimes an account will be logged in and able to add reviews, but the nav bar will show the log in
button, despite what the Jinja templating dictates. I've tested this by adding a review when the log in message is showing, and 
the review successfully displays the session.user as a author

3. Password editing submissions