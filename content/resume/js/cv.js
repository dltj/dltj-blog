$('#btn-full-cv').on('click', function (e) {
	$('#btn-full-cv-li').toggleClass('active');
	$('#btn-brief-resume-li').toggleClass('active');
	var x = document.getElementsByClassName("cvonly");
	var i;
	for (i = 0; i < x.length; i++) {
    	$(x[i]).show('slow');
	}
	var y = document.getElementsByClassName("resumeonly");
	var i;
	for (i = 0; i < y.length; i++) {
    	$(y[i]).hide('slow');
	}
})

$('#btn-brief-resume').on('click', function (e) {
	$('#btn-full-cv-li').toggleClass('active');
	$('#btn-brief-resume-li').toggleClass('active');
	var x = document.getElementsByClassName("cvonly");
	var i;
	for (i = 0; i < x.length; i++) {
    	$(x[i]).hide('slow');
	}
	var y = document.getElementsByClassName("resumeonly");
	var i;
	for (i = 0; i < y.length; i++) {
    	$(y[i]).show('slow');
	}
})

$('#cv-menubar-top .nav a').on('click', function(){
    $(".cv-navbar").click();
});