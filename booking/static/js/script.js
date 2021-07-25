$(document).ready(function () {
    var url = new URL(document.URL);
    var c = url.searchParams.get("days");
    let days = 1;
    let ah = $('#ahref').data("href")
    if (c) {
        days = c
    }

    let v;
    let h;
    let sd = false, ed = false;


    v = $('.dropdown #1').data("cost")
    h = $('.dropdown #1').data("href")


    $('.wrapper-home .dropdown .btn').html($('.dropdown #1').html())
    $('.wrapper-home .done').attr("href", h)
    $('#ahref').attr("href", ah)
    $('.wrapper-home .total_cost_e').html($('.dropdown #1').data("cost") + " " + " млн сумов")
    $('.wrapper-room .total_cost_e').html($('.wrapper-room .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")
    $('.wrapper-booking .total_cost_e').html($('.wrapper-booking .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")


    let updateHref = () => {
        let _h = h;
        if (sd) {
            _h += `?sd=${sd}&ed=${ed}&days=${days}`;
        }
        $('.wrapper-home .done').attr("href", _h)
    };

    let updateAHref = () => {
        let _ah = ah;
        if (sd) {
            _ah += `?sd=${sd}&ed=${ed}&days=${days}`;
        }
        $('#ahref').attr("href", _ah)
    };


    $('#picker').daterangepicker({
            opens: 'center',
        }
        , function (start, end) {
            sd = start.format('MM-DD-YYYY');
            ed = end.format('MM-DD-YYYY');
            $(this).val("asdasd")
            days = (end - start + 1) / (1000 * 60 * 60 * 24) - 1;
            $('.total_cost_e').html(v * parseInt(days) + " " + " млн сумов")
            $('.wrapper-room .total_cost_e').html($('.wrapper-room .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")
            $('.wrapper-booking .total_cost_e').html($('.wrapper-booking .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")
            $('[name = "days"]').val(days)
            $('[name = "start_date"]').val(sd)
            $('[name = "finish_date"]').val(ed)

            updateAHref();
            updateHref();
            // console.log(typeof parseInt($('.dropdown .dropdown-item').html()))
        }
    );


    $(' .dropdown .dropdown-item').on('click', function () {
        // alert(v)
        v = $(this).data("cost");
        h = $(this).data("href");

        updateAHref();
        updateHref();
        $('.wrapper-home .dropdown .btn').html($(this).html())
        $('.total_cost_e').html(parseInt(v) * parseInt(days) + " " + " млн сумов")
        $('.wrapper-room .total_cost_e').html($('.wrapper-room .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")
        $('.wrapper-booking .total_cost_e').html($('.wrapper-booking .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")


    })
    $('[name = "start_date"]').val(sd)
    $('[name = "finish_date"]').val(start)

    $('[name = "days"]').val(days)
    updateHref();
    updateAHref();
    // $('.dropdown .sect').on('click', function () {
    //     v = $(this).data("cost");
    //
    //     $('.total_cost_e').html(v * parseInt(days) + " " + " млн сумов")
    // })


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
