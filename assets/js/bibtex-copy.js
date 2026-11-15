(function () {
  'use strict';
  document.querySelectorAll('.pub-bibtex').forEach(function (details) {
    var button = details.querySelector('.pub-bibtex__copy');
    var code = details.querySelector('code');
    var status = details.querySelector('.pub-bibtex__status');
    if (!button || !code || !status) return;
    button.hidden = false;
    button.addEventListener('click', async function () {
      try {
        if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(code.textContent.trim() + '\n');
        status.textContent = 'Copied.';
      } catch (error) {
        var selection = window.getSelection();
        var range = document.createRange();
        range.selectNodeContents(code);
        selection.removeAllRanges();
        selection.addRange(range);
        status.textContent = 'Citation selected. Press Ctrl+C or ⌘C to copy.';
      }
    });
    details.addEventListener('toggle', function () {
      if (!details.open) status.textContent = '';
    });
  });
}());
