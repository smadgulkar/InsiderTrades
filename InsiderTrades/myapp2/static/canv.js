// function renderChart(data,labels){
// var chart = new CanvasJS.Chart("canvas", {        
//   data: [
//     {
//       type: "line",
//       dataPoints: [
//         1,2,3,4,5,5
//       ]
//     }         
//   ]
// });
// // }  

// $('#chartModal').on('shown.bs.modal', function () {
//   chart.render();
// });

// function getChartData() {
//     $("#loadingMessage").html('<img src="./static/giphy.gif" alt="" srcset="">');
//     jQuery.ajax({
//     	type: "GET",
//     	dataType: 'json',
//         url: "http://116.75.176.94:5000/quotes/500444",
//         success: function (result) {
//         	$("#loadingMessage").html("");
//         	var data = [], labels = [];
//             jQuery.each(result,function(index){
// 	            data.push(result[index].Close);
// 	        	labels.push(new Date(result[index].Date));
// 	            renderChart(data, labels);
//             });
//             // console.log(labels);  
//         },
//         error: function (err) {
//             $("#loadingMessage").html("Error");
//         }
//     });
// }

// $("#modal").on('shown.bs.modal', function() {
//     // console.log('create modal line in progress'); //this console logs out properly 
//    getChartData();

// });

window.onload = function () {
  var chart = new CanvasJS.Chart("canvas",
  {
    title: 
    {
      text: "Line Chart with Dashed line"             
    },
    data: [
    {        
      type: "line",
      lineDashType: "dash",              
      dataPoints: [
        { x: 10, y: 4 },
        { x: 20, y: 3 },
        { x: 30, y: 6 },
        { x: 40, y: 11},
        { x: 50, y: 21},
        { x: 60, y: 9 },
        { x: 70, y: 3 },
        { x: 80, y: 4 },
        { x: 90, y: 7 }
      ]
    } 
    ]
  });
  chart.render();
}
