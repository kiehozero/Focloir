/* jQuery for interactive design */

/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

/* Materialize jQuery intialisation */

$(document).ready(function(){
    /* initialises mobile side navigation bar */
    $('.sidenav').sidenav();
    /* initialises index.html parallax view */
    $('.parallax').parallax();
    /* initialises datepicker in review form */
    $('.datepicker').datepicker();
    /* initialises dropdown in add pub form */
    $('select').formSelect();
});

/* Navigation */
/* Need to ensure that button width stays the same when icon changes */

$("#pintButton").mouseenter(function(){
  $(this).html("<i class='fas fa-beer'></i>");
});
$("#pintButton").mouseleave(function(){
  $(this).html("Pints");
});

$("#pubButton").mouseenter(function(){
  $(this).html("<i class='fas fa-store-alt'></i>");
});
$("#pubButton").mouseleave(function(){
  $(this).html("Pubs");
});

$("#addButton").mouseenter(function(){
  $(this).html("<i class='fas fa-pen-nib'></i>");
});
$("#addButton").mouseleave(function(){
  $(this).html("Add a review");
});

$("#regButton").mouseenter(function(){
  $(this).html("<i class='fas fa-id-badge'></i>");
});
$("#regButton").mouseleave(function(){
  $(this).html("Register");
});

$("#myrButton").mouseenter(function(){
  $(this).html("<i class='fas fa-newspaper'></i>");
});
$("#myrButton").mouseleave(function(){
  $(this).html("My Reviews");
});

$("#logButton").mouseenter(function(){
  $(this).html("<i class='fas fa-sign-in-alt'></i>");
});
$("#logButton").mouseleave(function(){
  $(this).html("Log In");
});