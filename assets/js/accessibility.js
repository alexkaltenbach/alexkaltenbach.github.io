/* Keep the existing theme's menu controls accessible to assistive technology. */
(function () {
  'use strict';
  var navigationButton = document.querySelector('#site-nav button');
  var navigationLinks = document.getElementById('overflow-navigation');
  var authorButton = document.querySelector('.author__urls-wrapper button');
  var authorLinks = document.getElementById('author-links');

  function syncMenus() {
    if (navigationButton && navigationLinks) {
      navigationButton.setAttribute('aria-expanded', String(!navigationLinks.classList.contains('hidden')));
    }
    if (authorButton && authorLinks) {
      authorButton.setAttribute('aria-expanded', String(window.getComputedStyle(authorLinks).display !== 'none'));
    }
  }
  var observer = new MutationObserver(syncMenus);
  [navigationLinks, authorLinks].forEach(function (element) {
    if (element) observer.observe(element, {attributes: true, attributeFilter: ['class', 'style']});
  });
  window.addEventListener('resize', syncMenus);
  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;
    if (navigationLinks && !navigationLinks.classList.contains('hidden')) {
      navigationButton.click();
      navigationButton.focus();
    } else if (authorButton && authorButton.classList.contains('open')) {
      authorButton.click();
      authorButton.focus();
    }
  });
  syncMenus();
}());
