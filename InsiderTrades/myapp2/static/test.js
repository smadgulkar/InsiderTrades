const url = 'http://116.75.176.94:5000/quotes/500444';
// fetch(url).then(response => {
// 	return response;
// })
// .catch(err => console.log(err));


// // .then(function(data){
// 	// console.log(data.Close);
// // })

$("button").click(function(){
	jQuery.getJSON(url,function(data){
		jQuery.each(data,function(index){
			console.log(data[index].Close);
		});
		
	});
});
