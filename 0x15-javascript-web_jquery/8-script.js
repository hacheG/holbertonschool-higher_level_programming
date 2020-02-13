$(document).ready(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data) {
    for (let i = 0; i < data.results.length; i++) {
      $('ul#list_movies').append(data.results[i].title + '</br>');
    }
  });
});
