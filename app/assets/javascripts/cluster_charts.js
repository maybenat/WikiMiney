function getCluster() {
  var json = $.getJSON("/data/cluster/2008/october",
    function() {
      toPlot = [];
      for (var i = 0; i < 10; i++) { 
        toPlot.push([i, i]);
      }

      // Create the clusters
      $('#cluster').highcharts({
        chart: {
          type: 'scatter',
          zoomType: 'xy'
        },
        title: {text: 'Cluster'},
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
              pointFormat: '<b>{point.name}</b> Bytes: {point.x}, {point.y} views'
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
          data: toPlot,
        }],
      });
    }
  )
}
