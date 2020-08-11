function currentTime() {
    let now = moment()
    let displayTime = (now.format("MMMM Do, h:mm a"))
    document.getElementById('time').innerHTML = displayTime
}
currentTime()
setInterval(currentTime, 60000);

window.initMap = function () {
    navigator.geolocation.getCurrentPosition(position => {
        let user_latitude = position.coords.latitude
        let user_longitude = position.coords.longitude
        let user_coords = { lat: user_latitude, lng: user_longitude }
        map = new google.maps.Map(document.getElementById('map'), {
            center: user_coords,
            zoom: 13,
            disableDefaultUI: true,
        });
        let bikeLayer = new google.maps.BicyclingLayer();
        bikeLayer.setMap(map);
        let user_coords_marker = new google.maps.Marker({
            position: user_coords,
            map: map,
            title: 'Your location!',
            icon: {
                animation: google.maps.Animation.DROP,
                url: "/static/girodm/images/streetview_icon.png",
                scaledSize: new google.maps.Size(40, 40),
            }

        });

        // gets axios response from own database, sets a marker for each ride on the map with a clickable link to the ride.
        axios({
            url: "/getlatlng/",
            method: 'get'
        }).then(response => {
            console.log(response)
            let startLocations = response.data.start_location_list
            let ridesToday = []
            let now = moment()
            for (let i = 0; i < startLocations.length; ++i) {
                let ride = startLocations[i]
                let dateTime = ride.date
                let rideDated = dateTime.split("T")
                let dateOfRide = rideDated[0]
                let formattedRideDate = moment(dateOfRide).format("MM-DD-YYYY")
                let formattedTodaysDate = now.format("MM-DD-YYYY")
                if (formattedTodaysDate === formattedRideDate) {
                    ridesToday.push(ride)
                }
            }
            console.log(ridesToday)
            for (let i = 0; i < ridesToday.length; ++i) {
                let rideToday = ridesToday[i]
                let marker = new google.maps.Marker({
                    position: { lat: rideToday.lat, lng: rideToday.lng },
                    animation: google.maps.Animation.DROP,
                    title: rideToday.label,
                    map: map,
                    icon: {
                        url: "/static/girodm/images/future_logo.png",
                        scaledSize: new google.maps.Size(60, 40),
                    },
                })
                google.maps.event.addListener(marker, 'click', function () {
                    window.location.href = rideToday.url;
                })
            }
        })
    })
}