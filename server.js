const express = require("express");
const app = express();
const port = 3000;
const { spawn } = require("child_process");
const cors = require("cors");
const bodyParser = require("body-parser");

app.use(bodyParser.json());
app.use(cors());

app.post("/api/bet", (req, res) => {
  //const { array } = req.body;
  ///const data = req.body.data;

  const data = [
    {
      siteName: "spreadex",
      homeWin: 1850,
      draw: 3750,
      awayWin: 3750,
      money: 1000,
    },
    {
      siteName: "888sport",
      homeWin: 935,
      draw: 1975,
      awayWin: 1975,
      money: 500,
    },
    {
      siteName: "unibet",
      homeWin: 3800,
      draw: 8000,
      awayWin: 7600,
      money: 2000,
    },
    {
      siteName: "leovegas",
      homeWin: 1900,
      draw: 4030,
      awayWin: 3780,
      money: 1000,
    },
    {
      siteName: "comeOn",
      homeWin: 1850,
      draw: 3900,
      awayWin: 3900,
      money: 1000,
    },
    {
      siteName: "bwin",
      homeWin: 1900,
      draw: 3950,
      awayWin: 3700,
      money: 1000,
    },
    {
      siteName: "nordicBet",
      homeWin: 950,
      draw: 1965,
      awayWin: 1845,
      money: 500,
    },
    {
      siteName: "betsson",
      homeWin: 935,
      draw: 1950,
      awayWin: 1900,
      money: 500,
    },
    {
      siteName: "bet25",
      homeWin: 935,
      draw: 1975,
      awayWin: 1900,
      money: 1600,
    },
    {
      siteName: "expekt",
      homeWin: 1850,
      draw: 3900,
      awayWin: 3900,
      money: 1000,
    },
    {
      siteName: "cashpoint",
      homeWin: 915,
      draw: 2025,
      awayWin: 1985,
      money: 500,
    },
  ];
  console.log(data);
  const pythonProcess = spawn("python", ["test.py"]);
  pythonProcess.stdin.write(JSON.stringify(data));
  pythonProcess.stdin.end();

  pythonProcess.stdout.on("data", (data) => {
    console.log(`stdout: ${data}`);
    res.json({
      message: JSON.parse(data.toString()),
    });
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on("close", (code) => {
    console.log(`Child process exited with code ${code}`);
  });
  /* exec("python3 test.py", (error, stdout, stderr) => {
    if (error) {
      console.log(`error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.log(`stderr: ${stderr}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    res.json({
      message: stdout,
    });
  }); */
});

app.post("/", (req, res) => {
  res.json({
    message: "Hello World",
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
