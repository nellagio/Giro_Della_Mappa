window.initMap = function () {
    navigator.geolocation.getCurrentPosition(position => {
        let user_latitude = position.coords.latitude
        let user_longitude = position.coords.longitude
        let user_coords = { lat: user_latitude, lng: user_longitude }
        console.log(user_coords)
        map = new google.maps.Map(document.getElementById('map'), {
            center: user_coords,
            zoom: 13,
            disableDefaultUI: true,
        })
        let bikeLayer = new google.maps.BicyclingLayer()
        bikeLayer.setMap(map)
        let user_coords_marker = new google.maps.Marker({
            position: user_coords,
            map: map,
            title: 'Your location!',
            icon: {
                url: "/static/girodm/images/streetview_icon.png",
                scaledSize: new google.maps.Size(60, 40),
            }

        })

        // gets axios response from own database, sets a marker for each ride on the map with a clickable link to the ride.
        axios({
            url: "/getlatlng/",
            method: 'get'
        }).then(response => {
            console.log(response)
            let startLocations = response.data.start_location_list
            let upcomingRides = []
            let now = moment()
            for (let i = 0; i < startLocations.length; ++i) {
                let ride = startLocations[i]
                let dateTime = ride.date
                let rideDated = dateTime.split("T")
                let dateOfRide = rideDated[0]
                if (moment(dateOfRide).diff(now, 'days') >= 0) {
                    upcomingRides.push(ride)
                }
            }
            console.log(upcomingRides)
            for (let i = 0; i < upcomingRides.length; ++i) {
                let rideToday = upcomingRides[i]
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