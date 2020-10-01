##js file to get position

function(){
	var a=5
	var b=10
	console.log(10)
	if (navigator.geolocation){
		navigator.geolocation.GetCurrentPosition()
		latitude=position.coords.latitude
		console.log(latitude)
	}
}
