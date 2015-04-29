function getIndex(year, amount) {
  var pages, jsonData, frequencies, drilldownSeries, pagesData, date;;
  var json = $.getJSON("data/top/" + amount + "/year/" + year,
    function() {
      // Get top 50 most viewed pages in year and month
      jsonData = json.responseJSON;

      // Initialize
      arr = [];
      frequencies = [];
      pages = [];
      pagesData = [];
      drilldownSeries = [];
      date = [];

      // For each page
      for (var j in jsonData) {
        pages[j] = jsonData[j].page;

        // Load each all of the day views for each page within a month
        for (var k in jsonData[j].wikiviews) {
          if (!date[jsonData[j].page]) {
            date[jsonData[j].page] = [];
          }
          var day = jsonData[j].wikiviews[k].day;
          if (day === "all") {
            frequencies[j] = jsonData[j].wikiviews[k].views;
          } else {
            date[jsonData[j].page].push([
              jsonData[j].wikiviews[k].month + "/" + day,
              jsonData[j].wikiviews[k].views
            ]);

            drilldownSeries.push({
              name: pages[j],
              id: pages[j],
              data: date[pages[j]],
            });
          }
        }

        pagesData.push({
          name: pages[j],
          y: frequencies[j],
          drilldown: date[pages[j]] ? pages[j] : null
        });

        pagesData.sort(index_sort_by_y);
      }

      // Create the histogram
      $('#histogram-' + year).highcharts({
        chart: {type: 'column'},
        title: {text: 'Top ' + amount + ' Viewed Wikipages in ' + year},
        xAxis: {type: 'category'},
        yAxis: {
          title: {text: 'Total Views'}
        },
        legend: {enabled: true},
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
          series: {
            borderWidth: 0,
            dataLabels: {enabled: false}
          }
        },
        series: [{
          name: 'Frequencies',
          colorByPoint: true,
          data: pagesData,
        }],
        drilldown: {
          series: drilldownSeries,
        }
      });
    }
  )
}
