const API_URL = "http://localhost:8000/api/analytics/cmp_edc3151e";

fetch(API_URL)
  .then(res => res.json())
  .then(data => {
    document.getElementById("totalEvents").innerText = data.total_events;
    document.getElementById("publicViews").innerText = data.public_views;
    document.getElementById("verifyChecks").innerText = data.verify_checks;

    new Chart(document.getElementById("chart"), {
      type: "bar",
      data: {
        labels: ["Public Views", "Verify Checks"],
        datasets: [{
          label: "DPP Activity",
          data: [data.public_views, data.verify_checks]
        }]
      }
    });
  });
