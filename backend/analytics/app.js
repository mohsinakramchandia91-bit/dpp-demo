const API_BASE = "http://localhost:8000";
// Later yahan LIVE backend URL aayega

fetch(`${API_BASE}/api/analytics/cmp_textile_pk_001`)
  .then(res => res.json())
  .then(data => {
    document.getElementById("totalEvents").innerText = data.total_events;
    document.getElementById("publicViews").innerText = data.public_views;
    document.getElementById("verifyChecks").innerText = data.verify_checks;

    const ctx = document.getElementById("chart").getContext("2d");
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: ["Public Views", "Verify Checks"],
        datasets: [{
          label: "Activity",
          data: [data.public_views, data.verify_checks],
          backgroundColor: ["#22c55e", "#2563eb"]
        }]
      }
    });
  })
  .catch(err => console.error("API error:", err));
