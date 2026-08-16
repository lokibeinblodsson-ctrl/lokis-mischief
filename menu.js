/* menu.js — Loki's Mischief responsive nav.
   Injects a hamburger toggle into every existing <nav> (logo + .links pattern) and
   wires open/close. Pure progressive enhancement: if JS is off, the nav still shows
   links inline (we only hide .links via CSS at mobile widths when JS has marked the
   nav as js-enabled). Closing on link-click and on outside-tap keeps mobile UX clean. */
(function () {
  "use strict";
  function initNav(nav) {
    if (nav.dataset.navReady) return;
    var links = nav.querySelector(".links");
    if (!links) return;
    nav.classList.add("js-enabled");
    var btn = document.createElement("button");
    btn.className = "hamburger";
    btn.setAttribute("aria-label", "Toggle menu");
    btn.setAttribute("aria-expanded", "false");
    btn.setAttribute("aria-controls", "nav-links");
    links.id = links.id || "nav-links";
    btn.innerHTML = "<span></span><span></span><span></span>";
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // insert hamburger right after the logo
    var logo = nav.querySelector(".logo");
    if (logo && logo.nextSibling) nav.insertBefore(btn, logo.nextSibling);
    else nav.appendChild(btn);
    // close when a link is tapped
    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      }
    });
    nav.dataset.navReady = "1";
  }
  function initAll() {
    document.querySelectorAll("nav").forEach(initNav);
  }
  // close on outside tap
  document.addEventListener("click", function (e) {
    document.querySelectorAll("nav.open").forEach(function (nav) {
      if (!nav.contains(e.target)) {
        nav.classList.remove("open");
        var b = nav.querySelector(".hamburger");
        if (b) b.setAttribute("aria-expanded", "false");
      }
    });
  });
  if (document.readyState !== "loading") initAll();
  else document.addEventListener("DOMContentLoaded", initAll);
})();
