function articleList(id) {
	$.ajax({
		type : 'GET',
		url : "http://127.0.0.1:8000/api/articles/" + id + "/",
		success : function (resp) {
			console.log("resp is", resp);
			$('#title').text(resp.title);
			$('#pub_date').text(new Date(resp.pub_date.toLocaleString()));
			$('#body').text(resp.body);
			$('#image').attr('src', "/static/journal/images/" + resp.hero_image.split('/').pop())
			console.log();

		}
	});

};