const {spawn} = require('child_process');
chrome.runtime.onInstalled.addListener(() => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;
      console.log('URL actuelle :', currentUrl);
    });
  });

const url = currentUrl;
const pythonProcess = spawn('check.py', ['script.py', url]);

pythonProcess.stdout.on('data', (data) => {
    console.log(`Sortie du script Python : ${data}`);
});

pythonProcess.stderr.on('data', (data) => {
    console.error(`Erreur du script Python : ${data}`);
});