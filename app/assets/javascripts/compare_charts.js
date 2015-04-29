function compareMonths(page, month_r, year_r, month_b, year_b) {
  var url_r = "/data/search/project/en/page/" + page + "/year/" + year_r + "/month/" + month_r;
  var url_b = "/data/search/project/en/page/" + page + "/year/" + year_b + "/month/" + month_b;

  $.when($.getJSON(url_r), $.getJSON(url_b)).done(
    function(json_r, json_b) {
      var res_r = json_r[0][0];
      var res_b = json_b[0][0];

      var cats_r = build_categories_by_month(month_r, year_r);
      var cats_b = build_categories_by_month(month_b, year_b);
      var cats = build_categories_for_days();

      var toPlot_r = [];
      var toPlot_b = [];

      if (res_r) {
        var jsonData_r = res_r["wikiviews"];
        toPlot_r = build_column_data_with_cats(jsonData_r, cats_r);
      }

      if (res_b) {
        var jsonData_b = json_b[0][0]["wikiviews"];
        toPlot_b = build_column_data_with_cats(jsonData_b, cats_b);
      }

      // Create the histogram
      $('#compare').highcharts({
        chart: {type: 'column'},
        title: {text: page + " on " + month_r + "/" + year_r + " vs. " + month_b + "/" + year_b},
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
          name: month_r + "/dd/" + year_r,
          color: '#d9534f',
          data: toPlot_r,
        }, {
          name: month_b + "/dd/" + year_b,
          color: '#428bca',
          data: toPlot_b,
        }],
      });
    }
  )
}


function comparePages(page_r, page_b, month, year) {
  var url_r = "/data/search/project/en/page/" + page_r + "/year/" + year + "/month/" + month;
  var url_b = "/data/search/project/en/page/" + page_b + "/year/" + year + "/month/" + month;

  $.when($.getJSON(url_r), $.getJSON(url_b)).done(
    function(json_r, json_b) {
      var res_r = json_r[0][0];
      var res_b = json_b[0][0];

      var cats = build_categories_by_month(month, year);
      var toPlot_r = [];
      var toPlot_b = [];

      if (res_r) {
        var jsonData_r = res_r["wikiviews"];
        toPlot_r = build_column_data_with_cats(jsonData_r, cats);
      }

      if (res_b) {
        var jsonData_b = json_b[0][0]["wikiviews"];
        toPlot_b = build_column_data_with_cats(jsonData_b, cats);
      }

      // Create the histogram
      $('#compare').highcharts({
        chart: {type: 'column'},
        title: {text: page_r + " vs. " + page_b + " for " + month + "/" + year },
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
          name: page_r,
          color: '#d9534f',
          data: toPlot_r,
        }, {
          name: page_b,
          color: '#428bca',
          data: toPlot_b,
        }],
      });
    }
  )
}
