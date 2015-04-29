function search(month, year, day, page, project) {
  var json = $.getJSON("/data/search/project/" + project + "/page/" + page + "/year/" + year + "/month/" + month,
    function() {
      var res = json.responseJSON[0];
      var cats = build_categories_by_month(month, year);
      var toPlot = [];
      var jsonData, v;
      var search_title = project + "." + page + " on " + month + "/" + day + "/" + year;
      if (day == "all") {
        search_title = project + "." + page + " on " + month + "/" + year;
        if (res) {
          jsonData = res["wikiviews"];
          toPlot = build_column_data_with_cats(jsonData, cats);
        }
      } else if (res) {
        jsonData = res["wikiviews"];
        for (index in jsonData) {
          v = jsonData[index];
          if (v["month"] == month && v["day"] == day && v["year"] == year) {
            toPlot.push(v["views"]);
            cats = [month + "/" + day + "/" + year];
          }
        }
      }

      // Create the histogram
      $('#search').highcharts({
        chart: { type: 'column' },
        title: { text: search_title },
        xAxis: { categories: cats, crosshair: true },
        yAxis: {
          title: {text: 'Views'}
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
          name: "Page Views",
          data: toPlot,
        }],
      });
    }
  )
}
