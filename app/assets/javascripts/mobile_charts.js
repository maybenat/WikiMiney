function getMobile() {
  var json = $.getJSON("/data/progress/mobile",
    function() {
      var jsonData = json.responseJSON[0]["wikiviews"];
      var cats_08 = build_categories_by_year("2008");
      var cats_12 = build_categories_by_year("2012");
      var cats = cats_08.concat(cats_12);

      var toPlot = build_column_data_with_cats(jsonData, cats);

      // Create the histogram
      $('#mobile').highcharts({
        chart: {type: 'column'},
        title: {text: 'Wikipedia Mobile Views'},
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
