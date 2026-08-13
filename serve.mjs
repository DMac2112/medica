import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
const ROOT = path.resolve('.');
const PORT = 5177;
const TYPES = { '.html':'text/html','.css':'text/css','.js':'text/javascript','.woff2':'font/woff2','.svg':'image/svg+xml','.ico':'image/x-icon','.json':'application/json' };
http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p === '/') p = '/index.html';
  const fp = path.join(ROOT, p);
  if (!fp.startsWith(ROOT)) { res.writeHead(403); return res.end('no'); }
  fs.readFile(fp, (err, buf) => {
    if (err) { res.writeHead(404); return res.end('404'); }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(fp)] || 'application/octet-stream', 'Cache-Control':'no-cache' });
    res.end(buf);
  });
}).listen(PORT, () => console.log('serving http://localhost:'+PORT));
