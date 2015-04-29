function getCluster() {
  var json = $.getJSON("/data/cluster/2008/october",
    function() {
      jsonData = json.responseJSON;
      toPlot = [];

      clusts = [[], [], [], [], []];

      for (var index in jsonData) {
        page = jsonData[index]
        clst = parseInt(page["cluster"])
        clusts[clst].push({
          name: page["page"],
          x: page["views"],
          y: Math.round(page["bytes"] / page["views"])
        });
      }

      toPlot.push({name: "Cluster 1", color: 'rgba(255, 0, 0, 0.5)', data: clusts[0]});
      toPlot.push({name: "Cluster 2", color: 'rgba(0, 255, 0, 0.5)', data: clusts[1]});
      toPlot.push({name: "Cluster 3", color: 'rgba(0, 0, 255, 0.5)', data: clusts[2]});
      toPlot.push({name: "Cluster 4", color: 'rgba(255, 0, 255, 0.5)', data: clusts[3]});
      toPlot.push({name: "Cluster 5", color: 'rgba(0, 255, 255, 0.5)', data: clusts[4]});

      // Create the clusters
      $('#cluster').highcharts({
        chart: {
          type: 'scatter',
          zoomType: 'xy'
        },
        title: {text: 'Page Popularity vs. Page Size<br>using K-means++ Cluster'},
        xAxis: {
          title: {
            enabled: true,
            text: 'Views'
          },
          showLastLabel: true
        },
        yAxis: {
          title: {text: 'Bytes'}
        },
        plotOptions: {
          scatter: {
            turboThreshold: 0,
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
              pointFormat: '<b>{point.name}</b><br>{point.x} views, {point.y} bytes'
            },
            events: {
              click: function(event, i) {
                var win = window.open("http://www.en.wikipedia.org/wiki/" + event.point.name, '_blank');
                win.focus();
              }
            },
          }
        },
        series: toPlot,
      });
    }
  )
}
