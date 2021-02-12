/* jQuery for interactive design */

/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

/* Materialize jQuery intialisation */

/* Bugfix #8: variables below are used to set the maxDate for the datepicker */

var currYear = (new Date()).getFullYear();
var currMonth = (new Date()).getMonth();
var currDate = (new Date()).getDate();

$(document).ready(function(){
    /* initialises mobile side navigation bar */
    $('.sidenav').sidenav();
    /* initialises index.html parallax view */
    $('.parallax').parallax();
    /* initialises dropdown in add pub form */
    $('select').formSelect();
    /* initialises character countdown in review form */
    $('textarea#review').characterCounter();
    /* initialises datepicker in review form */
    $('.datepicker').datepicker({
        format: "yyyy-mm-dd",
        maxDate: new Date(currYear,currMonth, currDate),
        yearRange: [2016, currYear],
    });
});

/* Navigation */

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

$("#outButton").mouseenter(function(){
    $(this).html("<i class='fas fa-sign-out-alt'></i>");
});

$("#outButton").mouseleave(function(){
    $(this).html("Log Out");
});

$("#admButton").mouseenter(function(){
    $(this).html("<i class='fas fa-users-cog'></i>");
});

$("#admButton").mouseleave(function(){
    $(this).html("Users");
});

$("#pintButton").mouseenter(function(){
    $(this).html("<i class='fas fa-beer'></i>");
});

$("#pintButton").mouseleave(function(){
    $(this).html("Pints");
});


/* Mobile Only */
/* Need to extend for tablets */

if ($(window).width() < 602) {
    $(".admin-delete").html("<i class='far fa-trash-alt'></i>");
    $(".admin-moderate").html("<i class='far fa-edit'></i>");
    $("#searchButton").html("<i class='fas fa-search'></i>");
    $("#searchReset").html("<i class='fas fa-power-off'></i>");
    $(".user-delete").html("<i class='far fa-trash-alt'></i>");
    $(".user-edit").html("<i class='far fa-edit'></i>");
}