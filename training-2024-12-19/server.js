const https = require('node:https'); // HTTPS 모듈
const fs = require('node:fs');

// SSL 인증서와 키 파일 경로
const options = {
  key: fs.readFileSync('./public/ssl/localhost-key.pem'), // 개인 키 파일
  cert: fs.readFileSync('./public/ssl/localhost.pem') // 인증서 파일
};

const server = https.createServer(options, (req, res) => {
  if (req.method === "GET") {
    console.log(req.url);
    if (req.url === "/") {
      fs.readFile("./public/index.html", "utf-8", (err, data) => {
        if (err) throw err;
        res.writeHead(200, { "content-type": "text/html; charset=utf-8" });
        res.write(data);
        res.end();
      });
    }
    if (req.url === "/index.js") {
      fs.readFile("./public/index.js", "utf-8", (err, data) => {
        if (err) throw err;
        res.writeHead(200, { "content-type": "text/javascript; charset=utf-8" });
        res.write(data);
        res.end();
      });
    }
    if (req.url === "/test.js") {
      fs.readFile("./public/test.js", "utf-8", (err, data) => {
        if (err) throw err;
        res.writeHead(200, { "content-type": "text/javascript; charset=utf-8" });
        res.write(data);
        res.end();
      });
    }
    
  }

  if (req.method === "POST") {
    if (req.url === "/click") {
      console.log('클릭 누름');
      let minstone = "";
      req.on("data", (data) => {
        minstone += data;
      });
      req.on("end", () => {
        console.log('서버 작동 종료');
        console.log(minstone);
        res.end();
      });
    }
  }
});

// HTTPS 서버 실행
server.listen(3000, (err) => {
  if (err) throw err;
  console.log("https://localhost:3000");
});
