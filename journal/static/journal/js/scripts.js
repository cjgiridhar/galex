function articleDetail(id) {
	$.ajax({
		type : 'GET',
		//url: "https://protected-journey-8694.herokuapp.com/api/articles/" + id + "/",
		url : "/api/articles/" + id + "/",
		success : function (resp) {
			$('#title').text(resp.title);
			$('#pub_date').text(new Date(resp.pub_date.toLocaleString()));
			$('#body').text(resp.body);
			$('#image').attr('src', "/static/journal/images/" + resp.hero_image.split('/').pop())
			console.log();

		}
	});

};

function articleList () {
	var titles = [];
	var dates = [];
	var contents = [];
	var images = [];
	$.ajax({
		type : 'GET',
		//url: "https://protected-journey-8694.herokuapp.com/api/articles/" + id + "/",
		url : "http://127.0.0.1:8000/api/articles/",
		success : function (resp) {
			console.log("RESPO is:", resp[0]);
			$('#title' + '0').text(resp[0].title);
			// $('#pub_date').text(new Date(resp.pub_date.toLocaleString()));
			// $('#body').text(resp.body);
			// $('#image').attr('src', "/static/journal/images/" + resp.hero_image.split('/').pop())
			

		}
	});
}
