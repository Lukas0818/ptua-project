document.addEventListener("DOMContentLoaded", function() {
  var form = document.querySelector('.create-review form');
  var titleField = form.elements[form.title.name];
  var contentField = form.elements[form.content.name];
  var ratingField = form.elements[form.rating.name];
  var titleError = document.getElementById('titleError');
  var contentError = document.getElementById('contentError');
  var ratingError = document.getElementById('ratingError');

  form.addEventListener('submit', function(event) {
    var hasErrors = false;

    titleError.style.display = 'none';
    contentError.style.display = 'none';
    ratingError.style.display = 'none';

    if (titleField.value.trim() === '') {
      titleError.style.display = 'block';
      hasErrors = true;
    }

    if (contentField.value.trim() === '') {
      contentError.style.display = 'block';
      hasErrors = true;
    }

    var rating = parseInt(ratingField.value, 10);
    if (isNaN(rating) || rating < 1 || rating > 10) {
      ratingError.style.display = 'block';
      hasErrors = true;
    }

    if (hasErrors) {
      event.preventDefault();
      return;
    }

  });
});