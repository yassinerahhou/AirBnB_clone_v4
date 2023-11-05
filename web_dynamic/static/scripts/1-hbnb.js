// Your script must be executed only when DOM is loaded
// You must use JQuery
// Listen for changes on each input checkbox tag:
// if the checkbox is checked, you must store the Amenity ID in a variable (dictionary or list)
// if the checkbox is unchecked, you must remove the Amenity ID from the variable
// update the h4 tag inside the div Amenities with the list of Amenities checked

$(function () {
  const amenityObject = {};

  $('input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      amenityObject[$(this).data("id")] = $(this).data("name");
      $("div.amenities h4").text(Object.values(amenityObject).join(", "));
    } else if ($(this).is(":not(:checked)")) {
      delete amenityObject[$(this).data("id")];
      $("div.amenities h4").text(Object.values(amenityObject).join(", "));
    }
    console.log(amenityObject);
  });
});
