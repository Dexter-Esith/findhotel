/* HTML document is loaded. DOM is ready.
-----------------------------------------*/
$(document).ready(function () {
	// Mobile menu
	$(".mobile-menu-icon").click(function () {
		$(".tm-nav").toggleClass("show");
	});

	// http://stackoverflow.com/questions/2851663/how-do-i-simulate-a-hover-with-a-touch-in-touch-enabled-browsers
	$("body").bind("touchstart", function () {});
});

// Get the modal

// registraciis funqcia
let register_id = document.getElementById("register_id");
// loginis funqcia
let login_id = document.getElementById("login_id");
// registraciidan loginze gadasvlis funqcia
let register_to_login = document.getElementById("register_to_login");
// registraciisas infos amogdebis funqcia
let register_to_info = document.getElementById("register_to_info");

// modals garet dacheris shemdeg modalis chaxurvis funqcia

window.addEventListener("click", function (event) {
	if (event.target === login_id) {
		login_id.style.display = "none";
	} else if (event.target === register_id) {
		register_id.style.display = "none";
	} else if (event.target === register_to_login) {
		register_id.style.display = "none";
		login_id.style.display = "block";
	} else if (event.target === register_to_info) {
		register_id.style.display = "none";
		register_to_info.style.display = "block";
	}
});



// SEEMORE SLIDESHOW

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}