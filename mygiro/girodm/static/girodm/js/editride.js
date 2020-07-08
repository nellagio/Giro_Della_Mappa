window.initMap = function () {
    navigator.geolocation.getCurrentPosition(position => {
        let user_latitude = position.coords.latitude
        let user_longitude = position.coords.longitude
        let user_coords = { lat: user_latitude, lng: user_longitude }
        console.log(user_coords)
        map = new google.maps.Map(document.getElementById('map'), {
            center: user_coords,
            zoom: 12
        });
        let bikeLayer = new google.maps.BicyclingLayer();
        bikeLayer.setMap(map);
        var user_coords_marker = new google.maps.Marker({
            position: user_coords,
            map: map,
            title: 'Your location!'
        });
        // start coords
        var start_input = document.getElementById('autocompleteStart');
        var start_autocomplete = new google.maps.places.Autocomplete(start_input);
        start_autocomplete.setFields(['address_components', 'geometry', 'icon', 'name']);
        start_autocomplete.addListener('place_changed', function () {
            var start_place = start_autocomplete.getPlace();
            if (!start_place.geometry) {
                // User entered the name of a start_place that was not suggested and
                // pressed the Enter key, or the start_place Details request failed.
                window.alert("No details available for input: '" + start_place.name + "'");
                return;
            }

            // If the start_place has a geometry, then present it on a map.
            if (start_place.geometry.viewport) {
                map.fitBounds(start_place.geometry.viewport);
            } else {
                map.setCenter(start_place.geometry.location);
                map.setZoom(17);  // Why 17? Because it looks good.
            }

            var address = '';
            if (start_place.address_components) {
                address = [
                    (start_place.address_components[0] && start_place.address_components[0].short_name || ''),
                    (start_place.address_components[1] && start_place.address_components[1].short_name || ''),
                    (start_place.address_components[2] && start_place.address_components[2].short_name || '')
                ].join(' ')
                // console.log(start_place)
                var start_lat = start_place.geometry.location.lat()
                var start_lng = start_place.geometry.location.lng()
                var start_coords = { lat: start_lat, lng: start_lng }
                console.log(start_coords)
                console.log("start")
                var start_coords_marker = new google.maps.Marker({
                    position: start_coords,
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    map: map,
                    title: 'Where a ride starts'
                });
            }
        })

        // end coords

        var end_input = document.getElementById('autocompleteEnd');
        var end_autocomplete = new google.maps.places.Autocomplete(end_input);
        end_autocomplete.setFields(['address_components', 'geometry', 'icon', 'name']);

        end_autocomplete.addListener('place_changed', function () {
            var end_place = end_autocomplete.getPlace();
            if (!end_place.geometry) {
                // User entered the name of a end_place that was not suggested and
                // pressed the Enter key, or the end_place Details request failed.
                window.alert("No details available for input: '" + end_place.name + "'");
                return;
            }

            // If the end_place has a geometry, then present it on a map.
            if (end_place.geometry.viewport) {
                map.fitBounds(end_place.geometry.viewport);
            } else {
                map.setCenter(end_place.geometry.location);
                map.setZoom(17);  // Why 17? Because it looks good.
            }

            var address = '';
            if (end_place.address_components) {
                address = [
                    (end_place.address_components[0] && end_place.address_components[0].short_name || ''),
                    (end_place.address_components[1] && end_place.address_components[1].short_name || ''),
                    (end_place.address_components[2] && end_place.address_components[2].short_name || '')
                ].join(' ')
                // console.log(end_place)
                var end_lat = end_place.geometry.location.lat()
                var end_lng = end_place.geometry.location.lng()
                var end_coords = { lat: end_lat, lng: end_lng }
                console.log(end_coords)
                console.log("end")
                var end_coords_marker = new google.maps.Marker({
                    position: end_coords,
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    map: map,
                    title: 'Where the ride ends'
                });
            }
        })

    })
}
$(document).on("keydown", "form", function(event) { 
    return event.key != "Enter";
});