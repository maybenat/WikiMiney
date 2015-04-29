function doData(month, year, numIn) {
  var pages, jsonData, frequencies, drilldownSeries, pagesData, date, dayData, regress, byteSize, byteArr;
  var json = $.getJSON("/data/search/project/" + project + "/page/" + page + "/year/" + year + "/month/" + month,
    function() {
      // Get top 50 most viewed pages in year and month
      jsonData = json.responseJSON;

      // Initialize
      arr = [];
      frequencies = [];
      pages = [];
      byteSize = [];
      pagesData = [];
      drilldownSeries = [];
      date = [];
      dayData = [];
      byteArr = [];
      regress = [];

      // For each page
      for (var j in jsonData) {
        pages[j] = jsonData[j].page;
        test = [];
        test = jsonData[j].wikiviews[0].views;

        // Load each all of the day views for each page within a month
        for (var k in jsonData[j].wikiviews) {
          if (!date[jsonData[j].page]) {
            date[jsonData[j].page] = [];
          }
          var day = jsonData[j].wikiviews[k].day;

          var monthy = jsonData[j].wikiviews[k].month;
          var temp = month.toString();

          if ((monthy === temp) && (day === "all")) {
            frequencies[j] = jsonData[j].wikiviews[k].views;
          }

          if (!(day === "all")) {
            date[jsonData[j].page].push([jsonData[j].wikiviews[k].month + "/" + day, jsonData[j].wikiviews[k].views]);
            if (!dayData[jsonData[j].page]) {
              dayData[jsonData[j].page] = [];
            }

            var numViews = jsonData[j].wikiviews[k].views;
            var numBytes = jsonData[j].wikiviews[k].bytes;

            numBytes = numBytes.toFixed(2);
            if (!byteArr[jsonData[j].page]) {
              byteArr[jsonData[j].page] = [];
            }
            byteArr[jsonData[j].page].push(numBytes);
            dayData[jsonData[j].page].push(numViews);

            byteSize.push({
              name: pages[j],
              id: pages[j],
              data: byteArr[pages[j]]
            });

            drilldownSeries.push({
              name: pages[j],
              id: pages[j],
              data: date[pages[j]],
            });
          }
        }

        var fullBytes = (jsonData[j].wikiviews[k].bytes) / numViews;
        fullBytes = fullBytes.toFixed(2);

        regress.push({
          name: pages[j],
          id: pages[j],
          x: parseFloat(fullBytes),
          y: parseFloat(frequencies[j])
        });

        pagesData.push({
          name: pages[j],
          y: frequencies[j],
          drilldown: date[pages[j]] ? pages[j] : null
        });
      }

      // Create the histogram
      $('#histogram').highcharts({
        chart: {type: 'column'},
        title: {text: 'Wiki Views'},
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
        }, {
          name: 'Curve',
          type: 'spline',
          visible: false,
          data: frequencies,
        }, {
          name: 'Filled Curve',
          type: 'areaspline',
          visible: false,
          data: frequencies,
        }],
        drilldown: {
          series: drilldownSeries,
        }
      });

      // Create the regression
      $('#regression').highcharts({
        chart: {
          type: 'scatter',
          zoomType: 'xy'
        },
        title: {text: 'Top Page vs Views Regression Line'},
        xAxis: {
          title: {
            enabled: true,
            text: 'Bytes'
          },
          showLastLabel: true
        },
        yAxis: {
          title: {text: 'Views'}
        },
        legend: {
          layout: 'vertical',
          align: 'left',
          verticalAlign: 'top',
          floating: true,
          backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
          borderWidth: 1
        },
        plotOptions: {
          scatter: {
            marker: {
              radius: 5,
              states: {
                hover: {
                  enabled: true,
                  lineColor: 'rgb(100,100,100)'
                }
              }
            },
            states: {
              hover: {
                marker: {enabled: false}
              }
            },
            tooltip: {
              headerFormat: '',
              pointFormat: '<b> {point.name} </b> Bytes: {point.x}, {point.y} views'
            },
            events: {
              click: function(event, i) {
                var win = window.open("http://www.en.wikipedia.org/wiki/" + event.point.name, '_blank');
                win.focus();
              }
            },
          }
        },
        series: [{
          regression: true,
          regressionSettings: {
            type: 'linear',
            color: 'rgba(223, 83, 83, .9)',
          },
          colorByPoint: true,
          data: regress,
        }],
      });
    }
  )
}
