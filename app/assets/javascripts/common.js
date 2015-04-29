/* Frequently used helper functions */

function getData() {
  var month = document.getElementById("month-value").value;
  var year = document.getElementById("year-value").value;
  var pages = document.getElementById("pages-value").value;

  if (parseInt(month) && parseInt(year) && parseInt(pages)) {
    getTop(month, year, pages);
  }
}

function compareData() {
  var month = document.getElementById("month-value").value;
  var year = document.getElementById("year-value").value;
  var pages = document.getElementById("pages-value").value;

  if (parseInt(month) && parseInt(year) && parseInt(pages)) {
    getTop(month, year, pages);
  }
}

function toggleTab(tab) {
  if (tab === 'pom') {
    var el = document.getElementById('pom-tab');
    if (el) {
      el.className += el.className ? ' active' : 'active';
    }
    el = document.getElementById('ppm-tab');
    if (el) {
      el.className = '';
    }
    document.getElementById('page-over-months').style.display = "block";
    document.getElementById('pages-per-month').style.display = "none";
  } else if (tab === 'ppm') {
    var el = document.getElementById('ppm-tab');
    if (el) {
      el.className += el.className ? ' active' : 'active';
    }
    el = document.getElementById('pom-tab');
    if (el) {
      el.className = '';
    }
    document.getElementById('pages-per-month').style.display = "block";
    document.getElementById('page-over-months').style.display = "none";
  }
}

function index_sort_by_y(a, b) {
  if (a.y < b.y)
    return 1;
  if (a.y > b.y)
    return -1;
  return 0;
}

function build_categories_by_month(month, year) {
  var num_days = 30;
  var cats = [];
  if (month == "10" || month == "12") {
    num_days = 31;
  }
  for (var i = 1; i <= num_days; i++) {
    if (i < 10) {
      cats.push(month + "/0" + i + "/" + year);
    } else {
      cats.push(month + "/" + i + "/" + year);
    }
  }
  return cats;
}

function build_categories_by_year(year) {
  var oct = build_categories_by_month("10", year);
  var nov = build_categories_by_month("11", year);
  var dec = build_categories_by_month("12", year);
  var cats = [];
  cats.push.apply(cats, oct);
  cats.push.apply(cats, nov);
  cats.push.apply(cats, dec);
  return cats;
}

function build_categories_for_days() {
  var num_days = 31;
  var cats = [];
  for (var i = 1; i <= num_days; i++) {
    if (i < 10) {
      cats.push("mm/0" + i + "/yyyy");
    } else {
      cats.push("mm/" + i + "/yyyy");
    }
  }
  return cats;
}

function build_column_data_with_cats(json, cats) {
  var toPlot = [];
  var obj = {};
  var index, v, cat_key, date;

  for (index in json) {
    v = json[index];
    if (v["day"] != "all") {
      cat_key = v["month"] + "/" + v["day"] + "/" + v["year"]
      obj[cat_key] = v["views"];
    }
  }

  for (index in cats) {
    date = cats[index];
    if (obj[date]) {
      toPlot.push(obj[date]);
    } else {
      toPlot.push({});
    }
  }
  return toPlot;
}

function hideShowCompareHelp() {
  var load = document.getElementById("loading");
  var suggest = document.getElementById("suggest");

  if (load) {
    load.style.display = "block";
  }
  if (suggest) {
    suggest.style.display = "none";
  }

}

function compPa() {
  var page_r = document.getElementById("red-page-value").value;
  var page_b = document.getElementById("blue-page-value").value;
  var month = document.getElementById("month-value").value;
  var year = document.getElementById("year-value").value;

  if (page_r && page_b && month && year) {
    hideShowCompareHelp();
    comparePages(page_r, page_b, month, year);
  }
}


function compMo() {
  var page = document.getElementById("page-value").value;
  var month_r = document.getElementById("red-month-value").value;
  var year_r = document.getElementById("red-year-value").value;
  var month_b = document.getElementById("blue-month-value").value;
  var year_b = document.getElementById("blue-year-value").value;

  if (page && month_r && year_r && month_b && year_b) {
    hideShowCompareHelp();
    compareMonths(page, month_r, year_r, month_b, year_b);
  }
}
