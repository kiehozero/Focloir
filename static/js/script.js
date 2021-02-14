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
    /* initialised modals for confirmation buttons */
    $('.modal').modal();
});

/* Navigation Bar */

$("#pubButton").mouseenter(function(){
   $(this).html("<i class='fas fa-store-alt' aria-label='Pubs'></i>");
});

$("#pubButton").mouseleave(function(){
    $(this).html("Pubs");
});

$("#addButton").mouseenter(function(){
    $(this).html("<i class='fas fa-pen-nib' aria-label='Add a review'></i>");
});

$("#addButton").mouseleave(function(){
    $(this).html("Add a review");
});

$("#regButton").mouseenter(function(){
    $(this).html("<i class='fas fa-id-badge' aria-label='Register'></i>");
});

$("#regButton").mouseleave(function(){
    $(this).html("Register");
});

$("#myrButton").mouseenter(function(){
    $(this).html("<i class='fas fa-newspaper' aria-label='My Reviews'></i>");
});

$("#myrButton").mouseleave(function(){
    $(this).html("My Reviews");
});

$("#logButton").mouseenter(function(){
    $(this).html("<i class='fas fa-sign-in-alt' aria-label='Log In'></i>");
});

$("#logButton").mouseleave(function(){
    $(this).html("Log In");
});

$("#outButton").mouseenter(function(){
    $(this).html("<i class='fas fa-sign-out-alt' aria-label='Log Out'></i>");
});

$("#outButton").mouseleave(function(){
    $(this).html("Log Out");
});

$("#admButton").mouseenter(function(){
    $(this).html("<i class='fas fa-users-cog' aria-label='Users'></i>");
});

$("#admButton").mouseleave(function(){
    $(this).html("Users");
});

/* Flash bar */

$("#closeButton").click(function(){
    $("#message-row").css("display", "none");
})


/* Tablet Only */

if ($(window).width() < 1280) {
    $(".admin-delete").html("<i class='far fa-trash-alt' aria-label='Admin Delete Entry'></i>");
    $(".admin-moderate").html("<i class='far fa-edit' aria-label='Admin Moderate Entry'></i>");
    $("#searchButton").html("<i class='fas fa-search' aria-label='Search Pubs'></i>");
    $("#searchReset").html("<i class='fas fa-power-off' aria-label='Reset Search Criteria'></i>");
    $(".user-delete").html("<i class='far fa-trash-alt' aria-label='Delete Review'></i>");
    $(".user-edit").html("<i class='far fa-edit' aria-label='Edit Review'></i>");
    $(".read-more").html("Read").css("font-size", "16px");
}