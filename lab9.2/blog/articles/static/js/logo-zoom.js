$(document).ready(function () {

    const logo = $('.archive-logo');
    const images = $('.archive-parallax img');

    logo.hover(
        function () {
            $(this).css('transform', 'scale(1.05)');
        },
        function () {
            $(this).css('transform', 'scale(1)');
        }
    );


    images.each(function () {

        const originalWidth = $(this).width();

        $(this).hover(
            function () {

                $(this).stop().animate({
                    width: originalWidth + 20
                }, 300);

            },
            function () {

                $(this).stop().animate({
                    width: originalWidth
                }, 300);

            }
        );

    });

});