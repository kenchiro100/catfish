const {spawn} = require('child_process');
chrome.runtime.onInstalled.addListener(() => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;
      console.log('URL actuelle :', currentUrl);
    });
  });
// Récupère l'URL de la page actuelle
var url = window.location.href;

// Envoie l'URL à l'API de messagerie de l'extension (par exemple)
chrome.runtime.sendMessage({url: url});