
// adding osm tile 
var map = L.map("demo").setView([57.74, 11.94],8);
var baselayer=L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);



// getting the position of user
function getlocation(){
	var a =10
	var b=20
	console.log(a+b)
	myfunction()
	var x = document.getElementById("position");
	function myfunction() {
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(showPosition);
			
		}
		else { 
			x.innerHTML = "Geolocation is not supported by this browser.";
		}
	}

	function showPosition(position) {
		const lat= position.coords.latitude
		const lon=position.coords.longitude
		var position={"latitude":lat, "longitude": lon}
		x.innerHTML = "Latitude: " + position.latitude + 
		"<br>Longitude: " + position.longitude;
		console.log(lat)
	}	
}
function getocation(){
	var a =10
	var b=20
	console.log(a+b)
	myfunction()
	var x = document.getElementById("position");
	function myfunction() {
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(showPosition);
			
		}
		else { 
			x.innerHTML = "Geolocation is not supported by this browser.";
		}
	}

	function showPosition(position) {
		const lat= position.coords.latitude
		const lon=position.coords.longitude
		var position={"latitude":lat, "longitude": lon}
		x.innerHTML = "Latitude: " + position.latitude + 
		"<br>Longitude: " + position.longitude;
		console.log(lat)
		routing(position)
	}

	//routing between two points
	function routing(position){
		
		const lat=position.latitude
		const lon=position.longitude
		console.log(lat)
		console.log(lon)
		L.Routing.control({
			waypoints:[
			L.latLng(lat, lon),
			L.latLng(28.6792, 83.249)
			],
			routeWhileDragging: true,
		// geocoder: L.Control.Geocoder.nominatim()
			}).addTo(map);
	}

}


getocation()




