const url = 'http://116.75.176.94:5000/quotes/500444';

$("button").click(function(){
    jQuery.getJSON(url,function(data){
        jQuery.each(data,function(index){
            // console.log(data[index].Close);
            // var chartData=data[index].Close;
            var chartLabels=data[index].Date;
           $("#modal").on('shown.bs.modal', function() {
                // console.log('create modal line in progress'); //this console logs out properly 
                console.info();
            var data = {
                labels: ["2015", "2016", "2017", "2018", "2019"],
                // labels: [chartLabels],
                datasets: [
                    {
                        label: "My First dataset",
                        fillColor: "rgba(220,220,220,0.2)",
                        strokeColor: "rgba(220,220,220,1)",
                        pointColor: "rgba(220,220,220,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(220,220,220,1)",
                        data: [65, 59, 80, 81, 56, 55, 40]
                        // data: chartData.slice(-5),
                        
                    },
                // options: {
                //     animation: {
                //         duration: 2000, onProgress: function(animation) {
                //             progress.value = animation.currentStep / animation.numSteps;
                //         },
                //         onComplete: function(animation) {
                //             window.setTimeout(function() {
                //                 progress.value = 0;
                //             }, 2000);
                //         },
                //     }, 
                // },   

                    // {
                    //     label: "My Second dataset",
                    //     fillColor: "rgba(151,187,205,0.2)",
                    //     strokeColor: "rgba(151,187,205,1)",
                    //     pointColor: "rgba(151,187,205,1)",
                    //     pointStrokeColor: "#fff",
                    //     pointHighlightFill: "#fff",
                    //     pointHighlightStroke: "rgba(151,187,205,1)",
                    //     data: [28, 48, 40, 19, 86, 27, 90]
                    // }
                ]
            };

            var ctx = document.getElementById('canvas').getContext('2d');
            var myLineChart = new Chart(ctx, {
            	type: 'line',
            	data: data,
            });
            });

        });
        
    });
});
