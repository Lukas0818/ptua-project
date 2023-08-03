$(document).ready(function() {
  var pricePerDayElement = $("#pricePerDay");
  var pricePerDay = pricePerDayElement.data("price");
  $("#id_start_date, #id_end_date").datepicker($.extend({dateFormat: "yy-mm-dd"}));

  function updatePrice() {
      var startDate = $("#id_start_date").val();
      var endDate = $("#id_end_date").val();
      var days = (new Date(endDate) - new Date(startDate)) / (1000 * 60 * 60 * 24);
      var totalPrice = days * pricePerDay;
      if (totalPrice > 0) {
        $("#total_price").text("Nauja kaina: " + totalPrice + " €");
      }
  }

  $("#id_start_date, #id_end_date").change(updatePrice);
  updatePrice();
});
