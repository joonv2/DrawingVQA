(function () {
  var navToggle = document.querySelector(".nav-toggle");
  var navLinks = document.querySelector(".nav-links");
  var yearNode = document.getElementById("year");
  var copyButton = document.querySelector(".copy-button");
  var copyTarget = document.getElementById("citation-code");

  if (yearNode) {
    yearNode.textContent = String(new Date().getFullYear());
  }

  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      var isOpen = navLinks.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    navLinks.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        navLinks.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  if (copyButton && copyTarget && navigator.clipboard) {
    copyButton.addEventListener("click", function () {
      navigator.clipboard.writeText(copyTarget.textContent || "").then(function () {
        copyButton.textContent = "Copied";
        window.setTimeout(function () {
          copyButton.textContent = "Copy BibTeX";
        }, 1600);
      });
    });
  }
}());
