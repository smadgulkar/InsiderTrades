function renderChart(data, labels) {
    var ctx = document.getElementById("canvas").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Daily Closing Prices',
                    data: data,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                },
            //     {
            //         label: 'Last week',
            //         data: data[1],
            //         borderColor: 'rgba(192, 192, 192, 1)',
            //         backgroundColor: 'rgba(192, 192, 192, 0.2)',
            //     }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        // callback: function (value, index, values) {
                        //     return float2dollar(value);
                        // }
                    }
                }]
            },
        }
    });
}

function getChartData() {
    $("#loadingMessage").html('<img src="./static/giphy.gif" alt="" srcset="">');
    jQuery.ajax({
    	type: "GET",
    	dataType: 'json',
        url: "http://116.75.176.94:5000/quotes/500444",
        success: function (result) {
        	$("#loadingMessage").html("");
        	var data = [], labels = [];
            jQuery.each(result,function(index){
	            data.push(result[index].Close);
	        	labels.push(new Date(result[index].Date));
	            renderChart(data, labels);
            });
            // console.log(labels);  
        },
        error: function (err) {
            $("#loadingMessage").html("Error");
        }
    });
}

$("#modal").on('shown.bs.modal', function() {
    // console.log('create modal line in progress'); //this console logs out properly 
   getChartData();

});

