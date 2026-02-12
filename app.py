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
(function () {
  const KEY = "mspfa_reader_id";

  let uid = localStorage.getItem(KEY);
  if (!uid) {
    uid = crypto.randomUUID();
    localStorage.setItem(KEY, uid);
  }

  fetch("https://mspfa-tracker.onrender.com/track", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      page: 1,              // номер страницы
      reader_id: uid
    })
  });
})();
</script>


</body>
</html>

