window.initMap = function () {

    let autoCompleteLatStart = document.querySelector('#autoCompleteLatStart')
    let autoCompleteLngStart = document.querySelector('#autoCompleteLngStart')
    let autoCompleteLatEnd = document.querySelector('#autoCompleteLatEnd')
    let autoCompleteLngEnd = document.querySelector('#autoCompleteLngEnd')

    navigator.geolocation.getCurrentPosition(position => {
        let user_latitude = position.coords.latitude
        let user_longitude = position.coords.longitude
        let user_coords = { lat: user_latitude, lng: user_longitude }
        console.log(user_coords)
        startMap = new google.maps.Map(document.getElementById('startMap'), {
            center: user_coords,
            zoom: 12
        });
        let bikeLayer = new google.maps.BicyclingLayer();
        bikeLayer.setMap(startMap);
        let user_coords_marker = new google.maps.Marker({
            position: user_coords,
            map: startMap,
            title: 'Your location!'
        });
        // start coords
        let start_input = document.getElementById('autocompleteStart');
        let start_autocomplete = new google.maps.places.Autocomplete(start_input);
        start_autocomplete.setFields(['address_components', 'geometry', 'icon', 'name']);
        start_autocomplete.addListener('place_changed', function () {
            let start_place = start_autocomplete.getPlace();
            if (!start_place.geometry) {
                // User entered the name of a start_place that was not suggested and
                // pressed the Enter key, or the start_place Details request failed.
                window.alert("No details available for input: '" + start_place.name + "'");
                return;
            }

            // If the start_place has a geometry, then present it on a map.
            if (start_place.geometry.viewport) {
                startMap.fitBounds(start_place.geometry.viewport);
            } else {
                startMap.setCenter(start_place.geometry.location);
                startMap.setZoom(17);  // Why 17? Because it looks good.
            }

            let address = '';
            if (start_place.address_components) {
                address = [
                    (start_place.address_components[0] && start_place.address_components[0].short_name || ''),
                    (start_place.address_components[1] && start_place.address_components[1].short_name || ''),
                    (start_place.address_components[2] && start_place.address_components[2].short_name || '')
                ].join(' ')
                
                let start_lat = start_place.geometry.location.lat()
                let start_lng = start_place.geometry.location.lng()
                autoCompleteLatStart.value = start_lat
                autoCompleteLngStart.value = start_lng
                let start_coords = { lat: start_lat, lng: start_lng }
                console.log(start_coords)
                console.log("start")

                let start_coords_marker = new google.maps.Marker({
                    position: start_coords,
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    map: startMap,
                    title: 'Where a ride starts',
                });
            }
        })

        // end coords
        endMap = new google.maps.Map(document.getElementById('endMap'), {
            center: user_coords,
            zoom: 12
        });
        let end_input = document.getElementById('autocompleteEnd');
        let end_autocomplete = new google.maps.places.Autocomplete(end_input);
        end_autocomplete.setFields(['address_components', 'geometry', 'icon', 'name']);

        end_autocomplete.addListener('place_changed', function () {
            let end_place = end_autocomplete.getPlace();
            if (!end_place.geometry) {
                // User entered the name of a end_place that was not suggested and
                // pressed the Enter key, or the end_place Details request failed.
                window.alert("No details available for input: '" + end_place.name + "'");
                return;
            }

            // If the end_place has a geometry, then present it on a map.
            if (end_place.geometry.viewport) {
                endMap.fitBounds(end_place.geometry.viewport);
            } else {
                endMap.setCenter(end_place.geometry.location);
                endMap.setZoom(17);  // Why 17? Because it looks good.
            }

            let address = '';
            if (end_place.address_components) {
                address = [
                    (end_place.address_components[0] && end_place.address_components[0].short_name || ''),
                    (end_place.address_components[1] && end_place.address_components[1].short_name || ''),
                    (end_place.address_components[2] && end_place.address_components[2].short_name || '')
                ].join(' ')
                // console.log(end_place)
                let end_lat = end_place.geometry.location.lat()
                let end_lng = end_place.geometry.location.lng()
                let end_coords = { lat: end_lat, lng: end_lng }
                autoCompleteLatEnd.value = end_lat
                autoCompleteLngEnd.value = end_lng
                console.log(end_coords)
                console.log("end")
                let end_coords_marker = new google.maps.Marker({
                    position: end_coords,
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    map: endMap,
                    title: 'Where the ride ends',
                });
            }
        })

    })
}
$(document).on("keydown", "form", function(event) { 
    return event.key != "Enter";
});