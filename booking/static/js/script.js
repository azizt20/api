$(document).ready(function () {
    let days = 1;
    let v;

// console.log()
    $('.dropdown .btn').html($('.dropdown #1').html())
    $('.total_cost_e').html($('.dropdown #1').data("cost") + " " + " млн сумов")
    $('.dropdown .blya').html($('.dropdown #1').data("cost") + "сумм/сутки")
    $('#opaae').html($('.dropdown #1').data("title"))


    $('#picker').daterangepicker({
            opens: 'center',
        }
        , function (start, end) {
            console.log(start._d)
            days = (end - start + 1) / (1000 * 60 * 60 * 24) - 1;
            $('.total_cost_e').html(parseInt(v) * parseInt(days) + " " + " млн сумов")
        }
    );


    $('.dropdown .dropdown-item').on('click', function () {
        var v = $(this).html();
        $('.dropdown .btn').html(v)
        $('#opaae').html($(this).data("title"))

    })

    $('.dropdown .sect').on('click', function () {
        v = $(this).data("cost");

        $('#opaae').html($(this).data("title"))
        $('.dropdown .blya').html(v + "сумм/сутки")
        $('.total_cost_e').html(parseInt(v) * parseInt(days) + " " + " млн сумов")
    })


// $(".mini-slider").slick({
//   dots: true,
//   infinite: true,
//   speed: 300,
//   slidesToShow: 1,
//   variableWidth: true,
//   startMode: true,
//   slidesToScroll: 1,
//   responsive: [
//     {
//       breakpoint: 1024,
//       settings: {
//         slidesToShow: 3,
//         slidesToScroll: 3,
//         infinite: true,
//         dots: true,
//       },
//     },
//     {
//       breakpoint: 600,
//       settings: {
//         slidesToShow: 2,
//         slidesToScroll: 2,
//       },
//     },
//     {
//       breakpoint: 480,
//       settings: {
//         // slidesToShow: 1,
//         variableWidth: true,

//         slidesToScroll: 1,
//       },
//     },

//   ],
// });


});
