const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT = 8000;
const HOST = 'localhost';
const DIRECTORY = __dirname;

// MIME types
const mimeTypes = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.css': 'text/css',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml'
};

const server = http.createServer((req, res) => {
  // Log request
  console.log(`[${new Date().toLocaleTimeString()}] ${req.method} ${req.url}`);

  // Prevent caching
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');

  // Default to pokemon-tactical-cheatsheet.html for root
  let filePath = req.url === '/'
    ? path.join(DIRECTORY, 'pokemon-tactical-cheatsheet.html')
    : path.join(DIRECTORY, req.url);

  console.log(`  📄 Serving: ${filePath}`);

  const ext = path.extname(filePath).toLowerCase();
  const contentType = mimeTypes[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404, { 'Content-Type': 'text/html' });
      res.end('<h1>404 - File Not Found</h1><p>Could not find: ' + req.url + '</p><p>Tried: ' + filePath + '</p>');
      console.log(`  ❌ 404 Not Found: ${filePath}`);
      return;
    }

    res.writeHead(200, { 'Content-Type': contentType });
    res.end(data);
    console.log(`  ✓ 200 OK (${data.length} bytes)`);
  });
});

server.listen(PORT, HOST, () => {
  const url = `http://${HOST}:${PORT}`;
  console.log('\n' + '='.repeat(60));
  console.log(`🚀 Server running at: ${url}`);
  console.log('='.repeat(60));
  console.log('\nPress Ctrl+C to stop the server\n');

  // Try to open in browser
  const cmd = process.platform === 'win32'
    ? `start ${url}`
    : process.platform === 'darwin'
      ? `open ${url}`
      : `xdg-open ${url}`;

  exec(cmd, (error) => {
    if (error) {
      console.log(`\n📌 If browser didn't open automatically, visit: ${url}`);
    }
  });
});

process.on('SIGINT', () => {
  console.log('\n\nShutting down server...');
  server.close();
  process.exit(0);
});
