$(function () {

    Highcharts.data({
        csv: document.getElementById('tsv').innerHTML,
        itemDelimiter: '\t',
        parsed: function (columns) {

            var pages = {},
                pagesData = [],
                date = {},
                drilldownSeries = [];

            columns[1] = $.map(columns[1], function (value) {
                    value = parseFloat(value);
                return value;
            });

            $.each(columns[0], function (i, name) {
                var page,
                    pageDate;

                if (i > 0) {

                    pageDate = name.match(/([0-9]+[\.0-9x]*)/);
                    if (pageDate) {
                        pageDate = pageDate[0];
                    }
                    page = name.replace(pageDate, '');

                    if (!pages[page]) {
                        pages[page] = columns[1][i];
                    } else {
                        pages[page] += columns[1][i];
                    }

                    if (pageDate !== null) {
                        if (!date[page]) {
                            date[page] = [];
                        }
                        date[page].push(['10/' + pageDate, columns[1][i]]);
                    }
                }

            });

            $.each(pages, function (name, y) {
                pagesData.push({
                    name: name,
                    y: y,
                    drilldown: date[name] ? name : null
                });
            });
            $.each(date, function (key, value) {
                drilldownSeries.push({
                    name: key,
                    id: key,
                    data: value
                });
            });

            // Create the chart
            $('#container').highcharts({
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Top Page Views, Oct 2012'
                },
                subtitle: {
                    text: 'Click the columns to view daily break down'
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
                    enabled: false
                },
                plotOptions: {
                    series: {
                        borderWidth: 0,
                        dataLabels: {
                            enabled: true,
                            format: '{point.y:.1f}'
                        }
                    }
                },

                tooltip: {
                    headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
                    pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}</b><br/>'
                },

                series: [{
                    name: 'Pages',
                    colorByPoint: true,
                    data: pagesData
                }],
                drilldown: {
                    series: drilldownSeries
                }
            });
        }
    });
});


