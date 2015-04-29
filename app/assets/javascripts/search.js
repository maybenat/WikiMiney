function search(month, year, dayIn, page, project) {
    var pages, jsonData, frequencies, drilldownSeries, pagesData, date, dayData, regress, byteSize, byteArr;
    var json = $.getJSON("/data/search/project/" + project + "/page/" + page + "/year/" + year + "/month/" + month,
        function() {
            jsonData = json.responseJSON;
            arr = [];
            frequencies = [];
            pages = [];
            byteSize = [];
            pagesData = [];
            drilldownSeries = [];
            date = [];
            dayData = [];
            byteArr = [];
            myDay = [0];


            if (parseInt(dayIn) < 10) {
                dayIn = "0" + dayIn.toString();
            }


            // For each page
            for (var j in jsonData) {
                var projecty = jsonData[j].project;
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
                    if ((monthy === temp) && (day === dayIn)) {
                        myDay[j] = jsonData[j].wikiviews[k].views;
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

                pagesData.push({
                    name: pages[j],
                    y: myDay[j],
                    drilldown: date[pages[j]] ? pages[j] : null
                });
            }

            // Create the histogram
            $('#results').highcharts({
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Wiki Views'
                },
                xAxis: {
                    type: 'category'
                },
                yAxis: {
                    title: {
                        text: 'Total Views'
                    }
                },
                legend: {
                    enabled: true
                },
                plotOptions: {
                    spline: {
                        shadow: false,
                        marker: {
                            radius: 1
                        }
                    },
                    areaspline: {
                        color: 'rgb(69, 114, 167)',
                        fillColor: 'rgba(69, 114, 167,.25)',
                        shadow: false,
                        marker: {
                            radius: 1
                        }
                    },
                    series: {
                        borderWidth: 0,
                        dataLabels: {
                            enabled: false
                        }
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
