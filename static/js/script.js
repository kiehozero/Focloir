/* jQuery for interactive design */

/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

$(document).ready(function(){
    $('.sidenav').sidenav();
});

/* add hover here to convert menu options to font awesome icons on hover */

$("#pintButton").mouseeenter(function(){
  $(this).html("Hello <b>world</b>!");
});