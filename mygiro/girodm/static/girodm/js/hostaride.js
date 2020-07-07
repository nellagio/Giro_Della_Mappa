window.initMap = function () {
    navigator.geolocation.getCurrentPosition(position => {
        let user_latitude = position.coords.latitude
        let user_longitude = position.coords.longitude
        let user_coords = { lat: user_latitude, lng: user_longitude }
        console.log(user_coords)
        map = new google.maps.Map(document.getElementById('map'), {
            center: user_coords,
            zoom: 13
        });
        let bikeLayer = new google.maps.BicyclingLayer();
        bikeLayer.setMap(map);

        var input = document.getElementById('autocompleteEnd');
        var autocomplete = new google.maps.places.Autocomplete(input);
        autocomplete.setFields(
            ['address_components', 'geometry', 'icon', 'name']);

        var input = document.getElementById('autocompleteStart');
        var autocomplete = new google.maps.places.Autocomplete(input);
        autocomplete.setFields(
            ['address_components', 'geometry', 'icon', 'name']);

        autocomplete.addListener('place_changed', function () {
            var place = autocomplete.getPlace();
            if (!place.geometry) {
                // User entered the name of a Place that was not suggested and
                // pressed the Enter key, or the Place Details request failed.
                window.alert("No details available for input: '" + place.name + "'");
                return;
            }

            // If the place has a geometry, then present it on a map.
            if (place.geometry.viewport) {
                map.fitBounds(place.geometry.viewport);
            } else {
                map.setCenter(place.geometry.location);
                map.setZoom(17);  // Why 17? Because it looks good.
            }

            var address = '';
            if (place.address_components) {
                address = [
                    (place.address_components[0] && place.address_components[0].short_name || ''),
                    (place.address_components[1] && place.address_components[1].short_name || ''),
                    (place.address_components[2] && place.address_components[2].short_name || '')
                ].join(' ')
                console.log(place)
                console.log(place.geometry.location.lat())
            }
        })
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition);
            } else {
                x.innerHTML = "Geolocation is not supported by this browser.";
            }
        }

        function showPosition(position) {

            let lat = position.coords.latitude;
            let long = position.coords.longitude;
            $("input[name='lat']").val(lat);
            $("input[name='lat']").val(long);
            let url_str = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + lat + ',' + long + '&key=yourkey'
            $.getJSON(url_str, function (data) {
                console.log(data);
                //here you get the location data, make more fields like street address, city in db and pass it to inputs and submit the form to save it.
            });
        }
    })
}