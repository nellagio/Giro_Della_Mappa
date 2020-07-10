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
        var user_coords_marker = new google.maps.Marker({
            position: user_coords,
            map: map,
            title: 'Your location!'
        });

        var input = document.getElementById('autocomplete');
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
                var end_lat = place.geometry.location.lat()
                var end_lng = place.geometry.location.lng()
                var end_coords = { lat: end_lat, lng: end_lng }
                console.log(end_coords)

                var start_coords_marker = new google.maps.Marker({
                    position: end_coords,
                    map: map,
                    title: 'Where a ride is'
                });
                function drop() {
                    for (var i = 0; i < markerArray.length; i++) {
                        setTimeout(function () {
                            addMarkerMethod();
                        }, i * 200);
                    }
                }
            }
        })

        axios({
            url: "/getlatlng/",
            method: 'get'
        }).then(response => {
            console.log(response)
        
            let startLocationLat = response.data.start_location_list[0].lat
            let startLocationLng = response.data.start_location_list[0].lng
            let endLocationLat = response.data.end_location_list[0].lat
            let endLocationLng = response.data.end_location_list[0].lng
            let marker = new google.maps.Marker({
                position: { lat: startLocationLat, lng: startLocationLng },
                animation: google.maps.Animation.DROP,
                label: response.data.start_location_list[0].label,
                map: map,
            })
        })
    })
}