<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>MSPFA Reader Stats</title>
<style>
  body {
    font-family: system-ui, sans-serif;
    background: #111;
    color: #eee;
    padding: 20px;
  }
  h1 {
    margin-top: 0;
  }
  .box {
    background: #1b1b1b;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
  }
  .bar {
    height: 22px;
    background: #333;
    border-radius: 4px;
    overflow: hidden;
    margin-top: 6px;
  }
  .fill {
    height: 100%;
    background: #e74c3c;
  }
  .page-title {
    display: flex;
    justify-content: space-between;
  }
</style>
</head>
<body>

<h1>📊 MSPFA Analytics</h1>

<div class="box">
  <strong>Уникальных читателей всего:</strong>
  <span id="total">—</span>
</div>

<div id="pages"></div>

<script>
fetch("https://mspfa-tracker.onrender.com/stats")
  .then(r => r.json())
  .then(data => {
    document.getElementById("total").textContent =
      data.total_unique_readers;

    const max = Math.max(
      ...data.pages.map(p => p.unique_readers)
    );

    const container = document.getElementById("pages");

    data.pages.forEach(p => {
      const percent = max
        ? Math.round((p.unique_readers / max) * 100)
        : 0;

      const box = document.createElement("div");
      box.className = "box";

      box.innerHTML = `
        <div class="page-title">
          <strong>Страница ${p.page}</strong>
          <span>${p.unique_readers}</span>
        </div>
        <div class="bar">
          <div class="fill" style="width:${percent}%"></div>
        </div>
      `;

      container.appendChild(box);
    });
  })
  .catch(() => {
    document.getElementById("total").textContent = "ошибка загрузки";
  });
</script>

</body>
</html>
