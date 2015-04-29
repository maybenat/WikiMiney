function getMobile() {
  var json = $.getJSON("/data/progress/mobile",
    function() {
      jsonData = json.responseJSON[0]["wikiviews"];
      toPlot = [];
      cats = [];

      for (var index in jsonData) {
        v = jsonData[index]
        if (v["day"] != "all") {
          toPlot.push(v["views"]);
          cats.push(v["month"] + "/" + v["day"] + "/" + v["year"]);
        }
      }

      // Create the histogram
      $('#mobile').highcharts({
        chart: {type: 'column'},
        title: {text: 'Mobile Use'},
        xAxis: { categories: cats, crosshair: true },
        yAxis: {
          title: {text: 'Total Views'}
        },
        plotOptions: {
          spline: {
            shadow: false,
            marker: {radius: 1}
          },
          areaspline: {
            color: 'rgb(69, 114, 167)',
            fillColor: 'rgba(69, 114, 167,.25)',
            shadow: false,
            marker: {radius: 1}
          },
        },
        series: [{
          name: 'Mobile Views',
          data: toPlot,
        }],
      });
    }
  )
}
