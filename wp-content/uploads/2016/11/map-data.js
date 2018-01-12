function initMap() {
  var uluru = {lat: 21.8677672, lng: 111.9631277};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 17,
    center: uluru,
    mapTypeId: 'hybrid',
  });
  var marker = new google.maps.Marker({
    position: uluru,
    map: map
  });
}

