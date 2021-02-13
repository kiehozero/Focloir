/* Scripts for contact form interactivity */

/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

/* Modal JS came from Tutorial Deep link in README */

$(document).ready(function() {
	$("#contact-footer").on("click", function() {
        $(".contact-modal").modal("show");
    });
});

/* EmailJS requests */

/* Copied from the Code Institute resume tutorial */

function sendMail(contactForm) {
    emailjs.send("gmail", "template_vn6mied", {
        "name": contactForm.name.value, 
        "email_address": contactForm.email.value, 
        "feedback": contactForm.feedback.value
    })
    .then(
        /* Bugfix #9: Tests responses, displays alert and hides modals if successful */
        function(response) {
            console.log("SUCCESS", response);
            alert("Goal! Message sent!");
            $("#full_name").val("");
            $("#email_address").val("");
            $("#feedback").val("");
            $(".contact-modal").modal("hide");
        },

        function(error) {
            alert("Yellow card! Please complete all fields.");
        }
    );
    return false;
}