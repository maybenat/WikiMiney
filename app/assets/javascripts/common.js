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

function index_sort_by_y(a,b) {
  if (a.y < b.y)
    return 1;
  if (a.y > b.y)
    return -1;
  return 0;
}
