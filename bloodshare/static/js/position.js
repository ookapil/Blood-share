

function getLocation(){
	var a=5
	var b=10
	console.log(a+b)
	if (navigator.geolocation){
		navigator.geolocation.GetCurrentPosition()
		latitude=position.coords.latitude
		console.log(latitude)
	}
}
