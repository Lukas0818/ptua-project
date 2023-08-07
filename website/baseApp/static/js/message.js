document.getElementById('sendMessageBtn').addEventListener('click', function () {
  var form = document.getElementById('contactForm');
  var formData = new FormData(form);
  var nameField = form.elements.name;
  var emailField = form.elements.email;
  var messageField = form.elements.message;
  var nameError = document.getElementById('nameError');
  var emailError = document.getElementById('emailError');
  var messageError = document.getElementById('messageError');
  nameError.style.display = 'none';
  emailError.style.display = 'none';
  messageError.style.display = 'none';

  if (nameField.value.trim() === '') {
    nameError.style.display = 'block';
    return;
  }

  if (!isValidEmail(emailField.value)) {
    emailError.style.display = 'block';
    return;
  }

  if (messageField.value.trim() === '') {
    messageError.style.display = 'block';
    return;
  }

  var xhr = new XMLHttpRequest();
  xhr.open('POST', form.action, true);
  xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      var response = JSON.parse(xhr.responseText);
      var messageDisplay = document.getElementById('messageDisplay');
      if (response.status === 'success') {
        messageDisplay.innerHTML = '<p class="success-message">Jūsų pranešimas gautas.</p>';
        form.reset();
      } else {
        messageDisplay.innerHTML = '<p class="error-message">' + response.message + '</p>';
      }
    }
  };
  xhr.send(formData);
});

function isValidEmail(email) {
  var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailPattern.test(email);
}
