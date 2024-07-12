const express = require("express");
const app = express();
const port = 3000;
const { spawn } = require("child_process");
const cors = require("cors");

app.use(cors());

app.get("/api/bet", (req, res) => {
  const data = JSON.parse(req.query.data);

  data.forEach((customerData) => {
    customerData.forEach((element) => {
      element.homeWin = parseInt(element.homeWin);
      element.draw = parseInt(element.draw);
      element.awayWin = parseInt(element.awayWin);
      element.money = parseInt(element.money);
    });
  });

  const pythonProcess = spawn("python", ["test.py"]);
  pythonProcess.stdin.write(JSON.stringify(data));
  pythonProcess.stdin.end();

  pythonProcess.stdout.on("data", (data) => {
    console.log(`stdout: ${data}`);
    res.json(JSON.parse(data.toString()));
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
    res.status(500).json({
      message: "Error",
    });
  });

  pythonProcess.on("close", (code) => {
    console.log(`Child process exited with code ${code}`);
  });
});

app.post("/api/test", (req, res) => {
  res.json({
    message: "Hello World",
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
