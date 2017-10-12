/**
 * Created by FROI on 10/4/2017.
 */


$(window).scroll(function () {
    if($(document).scrollTop() > 50)
    {
        $('nav').addClass('shrink');
    }
    else
    {
        $('nav').removeClass('shrink');
    }
    
});