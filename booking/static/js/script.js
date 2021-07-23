

$('.dropdown .dropdown-item').on('click', function() {
  var v = $(this).html();
  $('.dropdown .btn').html(v)
})

$('.dropdown .sect').on('click', function() {
  var v = $(this).data("cost");
  $('.dropdown .blya').html(v)
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
