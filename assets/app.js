/* =========================================================================
   Agentic AI Summit '26 Notes — page engine (vanilla, no build)

   Renders the current page (from <body data-page>) into <main id="page">
   using window.SITE_PAGES. Two renderers:
     · hub      — the overview home page
     · daypage  — one day × stage: sessions, searchable/filterable talk rows,
                  a detail <dialog> with TL;DR + deep links (#slug)
   All data-derived strings pass through LDW.escapeHtml before innerHTML.
   ========================================================================= */
(function () {
  "use strict";

  /* ---------- page-level i18n (chrome strings; content lives in data) ---------- */
  var I18N = {
    en: {
      searchPh: "Search talks, speakers, topics…",
      all: "All",
      results: "{n} / {m} talks",
      empty: "No talks match — try a different search.",
      am: "AM", pm: "PM",
      streamAm: "Morning stream", streamPm: "Afternoon stream",
      talks: "talks", sessions: "sessions",
      browse: "Browse by day & stage",
      browseKicker: "The index",
      quotesHead: "Voices from the stage",
      quotesKicker: "Pull quotes",
      aboutKicker: "Colophon",
      tldr: "TL;DR",
      topics: "Topics discussed",
      watch: "Watch from {t}",
      notes: "Full notes",
      inStream: "in the {half} stream",
      halfAm: "morning", halfPm: "afternoon",
      types: { keynote: "Keynote", talk: "Talk", panel: "Panel", workshop: "Workshop", fireside: "Fireside", misc: "Session" }
    },
    zh: {
      searchPh: "搜尋演講、講者、主題…",
      all: "全部",
      results: "{n} / {m} 場",
      empty: "沒有符合的演講——換個關鍵字試試。",
      am: "上午", pm: "下午",
      streamAm: "上午場直播", streamPm: "下午場直播",
      talks: "場", sessions: "個場次",
      browse: "依日期與舞台瀏覽",
      browseKicker: "索引",
      quotesHead: "台上的聲音",
      quotesKicker: "金句",
      aboutKicker: "關於",
      tldr: "重點速覽",
      topics: "討論主題",
      watch: "從 {t} 開始觀看",
      notes: "完整筆記",
      inStream: "{half}場直播",
      halfAm: "上午", halfPm: "下午",
      types: { keynote: "主題演講", talk: "演講", panel: "座談", workshop: "工作坊", fireside: "爐邊對談", misc: "其他" }
    }
  };

  var state = { search: "", type: "all" };
  var teardowns = [];

  function boot(fn) {
    if (window.LDW && window.LDW.ready) fn();
    else document.addEventListener("ldw:shell-ready", fn, { once: true });
  }

  boot(function () {
    var LDW = window.LDW;
    var t = LDW.t, esc = LDW.escapeHtml;
    var page = LDW.currentPage();
    var main = document.getElementById("page");
    if (!page || !main) return;

    function ui(key) { return (I18N[LDW.state.lang] || I18N.en)[key]; }
    function typeLabel(type) { return ui("types")[type] || ui("types").misc; }
    function fmt(str, map) {
      return String(str).replace(/\{(\w+)\}/g, function (_, k) { return map[k] != null ? map[k] : ""; });
    }
    function shortTime(hms) {
      if (!hms) return "—";
      var p = hms.split(":");
      return p.length === 3 ? p[0] + ":" + p[1] : hms;
    }

    /* ---------- scroll-entry reveals ---------- */
    function observeReveals(root) {
      var nodes = root.querySelectorAll(".reveal");
      if (!("IntersectionObserver" in window)) {
        nodes.forEach(function (n) { n.classList.add("is-in"); });
        return;
      }
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          /* reveal when entering the viewport OR already scrolled past it —
             otherwise fast scrolling leaves passed-over elements invisible */
          if (e.isIntersecting || e.boundingClientRect.top < 0) {
            e.target.classList.add("is-in");
            io.unobserve(e.target);
          }
        });
      }, { rootMargin: "0px 0px -6% 0px" });
      nodes.forEach(function (n, i) {
        n.style.setProperty("--reveal-delay", Math.min(i % 8, 6) * 45 + "ms");
        io.observe(n);
      });
      teardowns.push(function () { io.disconnect(); });
    }

    function teardown() {
      teardowns.forEach(function (fn) { try { fn(); } catch (e) {} });
      teardowns = [];
    }

    /* =====================================================================
       HUB (home)
       ===================================================================== */
    function renderHub() {
      var stageOrder = ["Plenary", "Atlas", "Nexus", "Compass"];
      var html = "";

      html += '<section class="hero reveal">' +
        '<p class="kicker">' + esc(t(page.hero.kicker)) + "</p>" +
        "<h1>" + esc(t(page.hero.heading)) + "</h1>" +
        '<p class="hero__lede">' + esc(t(page.hero.lede)) + "</p>" +
        "</section>";

      html += '<section class="stats">';
      page.stats.forEach(function (s) {
        html += '<div class="stat reveal" data-item>' +
          '<div class="stat__value">' + esc(s.value) + "</div>" +
          '<div class="stat__label">' + esc(t(s.label)) + "</div></div>";
      });
      html += "</section>";

      html += '<div class="sectionhead reveal"><h2>' + esc(ui("browse")) + "</h2>" +
        '<span class="kicker">' + esc(ui("browseKicker")) + "</span></div>";
      page.days.forEach(function (day) {
        html += '<div class="dayblock reveal"><h3>' + esc(t(day.label)) + "</h3>";
        day.pages.slice().sort(function (a, b) {
          return stageOrder.indexOf(a.stage) - stageOrder.indexOf(b.stage);
        }).forEach(function (p) {
          html += '<a class="dayrow reveal" data-item href="' + esc(p.slug) + '.html">' +
            '<span class="dayrow__dot stage-dot--' + esc(p.stage.toLowerCase()) + '"></span>' +
            '<span class="dayrow__stage">' + esc(p.stage) + " Stage</span>" +
            '<span class="dayrow__meta">' + p.count + " " + esc(ui("talks")) +
              " · " + p.sessions + " " + esc(ui("sessions")) + "</span>" +
            '<span class="material-symbols-rounded dayrow__arrow" aria-hidden="true">arrow_forward</span>' +
            "</a>";
        });
        html += "</div>";
      });

      if (page.quotes && page.quotes.length) {
        html += '<div class="sectionhead reveal"><h2>' + esc(ui("quotesHead")) + "</h2>" +
          '<span class="kicker">' + esc(ui("quotesKicker")) + "</span></div>" +
          '<section class="quotes">';
        page.quotes.forEach(function (q) {
          var gloss = t(q.gloss);
          html += '<figure class="quote reveal" data-item style="margin:0">' +
            '<blockquote class="quote__text" style="margin:0 0 14px">' + esc(q.text) + "</blockquote>" +
            '<figcaption class="quote__who"><strong>' + esc(q.speaker) + "</strong> · " + esc(q.affiliation) + "</figcaption>" +
            (gloss ? '<p class="quote__gloss">' + esc(gloss) + "</p>" : "") +
            "</figure>";
        });
        html += "</section>";
      }

      html += '<div class="sectionhead reveal"><h2>' + esc(t(page.about.heading)) + "</h2>" +
        '<span class="kicker">' + esc(ui("aboutKicker")) + "</span></div>" +
        '<section class="about reveal"><div></div><div class="about__body">';
      t(page.about.body).forEach(function (p) { html += "<p>" + esc(p) + "</p>"; });
      html += '<div class="about__links">';
      page.about.links.forEach(function (l) {
        html += '<a href="' + esc(l.href) + '" target="_blank" rel="noopener">' + esc(t(l.label)) + " ↗</a>";
      });
      html += "</div></div></section>";

      main.innerHTML = html;
      observeReveals(main);
    }

    /* =====================================================================
       DAY PAGE
       ===================================================================== */
    var allTalks = [];
    if (page.layout === "daypage") {
      page.sessions.forEach(function (s) {
        s.talks.forEach(function (tk) { allTalks.push(tk); });
      });
    }

    function talkMatches(tk) {
      if (state.type !== "all" && tk.type !== state.type) return false;
      if (!state.search) return true;
      var hay = [t(tk.title), tk.speaker, tk.affiliation, t(tk.summary), tk.session,
                 (tk.tags || []).join(" ")].join(" ").toLowerCase();
      return hay.indexOf(state.search.toLowerCase()) !== -1;
    }

    function presentTypes() {
      var seen = [];
      allTalks.forEach(function (tk) { if (seen.indexOf(tk.type) === -1) seen.push(tk.type); });
      var order = ["keynote", "talk", "panel", "fireside", "workshop", "misc"];
      return seen.sort(function (a, b) { return order.indexOf(a) - order.indexOf(b); });
    }

    function renderDay() {
      var visible = allTalks.filter(talkMatches);
      var visibleSlugs = {};
      visible.forEach(function (tk) { visibleSlugs[tk.slug] = true; });

      var html = "";
      html += '<header class="pagehead reveal">' +
        '<p class="kicker">' + esc(t(page.day)) + "</p>" +
        "<h1>" + esc(page.stage) + " Stage</h1>" +
        '<div class="pagehead__meta">' +
          "<span>" + page.count + " " + esc(ui("talks")) + " · " + page.sessions.length + " " + esc(ui("sessions")) + "</span>" +
          '<a href="' + esc(page.streams.am) + '" target="_blank" rel="noopener">' +
            '<span class="material-symbols-rounded" aria-hidden="true">play_circle</span>' + esc(ui("streamAm")) + "</a>" +
          '<a href="' + esc(page.streams.pm) + '" target="_blank" rel="noopener">' +
            '<span class="material-symbols-rounded" aria-hidden="true">play_circle</span>' + esc(ui("streamPm")) + "</a>" +
        "</div></header>";

      html += '<div class="controls">' +
        '<div class="searchwrap"><span class="material-symbols-rounded" aria-hidden="true">search</span>' +
          '<input id="search" type="search" placeholder="' + esc(ui("searchPh")) + '" value="' + esc(state.search) + '" aria-label="' + esc(ui("searchPh")) + '" /></div>' +
        '<div class="chiprow">' +
          '<button class="chip' + (state.type === "all" ? " active" : "") + '" data-filter="all" aria-pressed="' + (state.type === "all") + '">' + esc(ui("all")) + "</button>";
      presentTypes().forEach(function (ty) {
        html += '<button class="chip' + (state.type === ty ? " active" : "") + '" data-filter="' + esc(ty) + '" aria-pressed="' + (state.type === ty) + '">' + esc(typeLabel(ty)) + "</button>";
      });
      html += '<span class="result-count">' + esc(fmt(ui("results"), { n: visible.length, m: allTalks.length })) + "</span>" +
        "</div></div>";

      page.sessions.forEach(function (s) {
        var talks = s.talks.filter(function (tk) { return visibleSlugs[tk.slug]; });
        if (!talks.length) return;
        html += '<section class="session-group">' +
          '<div class="session-head">' +
            '<span class="session-head__half">' + esc(ui(s.half)) + "</span>" +
            '<span class="session-head__label">' + esc(s.label) + "</span>" +
          "</div>";
        talks.forEach(function (tk) {
          html += '<button class="card talkrow reveal" data-item data-slug="' + esc(tk.slug) + '" type="button">' +
            '<span class="talkrow__time">' + esc(shortTime(tk.start)) + "</span>" +
            '<span class="talkrow__main">' +
              '<span class="talkrow__title">' + esc(t(tk.title)) + "</span>" +
              '<span class="talkrow__speaker" style="display:block"><strong>' + esc(tk.speaker) + "</strong>" +
                (tk.affiliation ? " · " + esc(tk.affiliation) : "") + "</span>" +
              '<span class="talkrow__summary">' + esc(t(tk.summary)) + "</span>" +
            "</span>" +
            '<span class="badge badge--' + esc(tk.type) + '">' + esc(typeLabel(tk.type)) + "</span>" +
            "</button>";
        });
        html += "</section>";
      });

      if (!visible.length) html += '<p class="empty">' + esc(ui("empty")) + "</p>";

      main.innerHTML = html;
      wireDayEvents();
      observeReveals(main);
    }

    function wireDayEvents() {
      var search = document.getElementById("search");
      if (search) {
        search.addEventListener("input", function () {
          state.search = search.value;
          var pos = search.selectionStart;
          renderDay();
          var s2 = document.getElementById("search");
          if (s2) { s2.focus(); try { s2.setSelectionRange(pos, pos); } catch (e) {} }
        });
      }
      main.querySelectorAll(".chip").forEach(function (chip) {
        chip.addEventListener("click", function () {
          state.type = chip.getAttribute("data-filter");
          renderDay();
        });
      });
      main.querySelectorAll(".talkrow").forEach(function (row) {
        row.addEventListener("click", function () { openTalk(row.getAttribute("data-slug")); });
      });
    }

    /* ---------- talk detail dialog ---------- */
    function findTalk(slug) {
      for (var i = 0; i < allTalks.length; i++) if (allTalks[i].slug === slug) return allTalks[i];
      return null;
    }

    function openTalk(slug) {
      var tk = findTalk(slug);
      var dialog = LDW.dialog();
      if (!tk || !dialog) return;
      var body = document.getElementById("dialogBody");
      var halfWord = tk.half === "am" ? ui("halfAm") : ui("halfPm");
      var bullets = t(tk.tldr) || [];
      var html =
        '<div class="dialog__kicker">' +
          '<span class="badge badge--' + esc(tk.type) + '">' + esc(typeLabel(tk.type)) + "</span>" +
          '<span class="dialog__session">' + esc(tk.session) + "</span>" +
        "</div>" +
        "<h2>" + esc(t(tk.title)) + "</h2>" +
        '<p class="dialog__speaker"><strong>' + esc(tk.speaker) + "</strong>" +
          (tk.affiliation ? " — " + esc(tk.affiliation) : "") + "</p>" +
        '<p class="dialog__meta">' + esc(t(page.day)) + " · " + esc(page.stage) + " Stage · " +
          esc(tk.range || "") + " " + esc(fmt(ui("inStream"), { half: halfWord })) + "</p>" +
        '<div class="dialog__actions">' +
          '<a class="btn-primary" href="' + esc(tk.video) + '" target="_blank" rel="noopener">' +
            '<span class="material-symbols-rounded" aria-hidden="true">play_arrow</span>' +
            esc(fmt(ui("watch"), { t: tk.start || "00:00" })) + "</a>" +
          '<a class="btn-ghost" href="' + esc(tk.note) + '" target="_blank" rel="noopener">' +
            '<span class="material-symbols-rounded" aria-hidden="true">description</span>' +
            esc(ui("notes")) + " ↗</a>" +
        "</div>" +
        '<p class="dialog__summary">' + esc(t(tk.summary)) + "</p>";
      if (bullets.length) {
        html += '<p class="dialog__subhead">' + esc(tk.tldrKind === "topics" ? ui("topics") : ui("tldr")) + "</p>" +
          '<ul class="dialog__tldr">';
        bullets.forEach(function (b) { html += "<li>" + esc(b) + "</li>"; });
        html += "</ul>";
      }
      if (tk.tags && tk.tags.length) {
        html += '<div class="dialog__tags">';
        tk.tags.forEach(function (tg) { html += '<span class="tag">' + esc(tg) + "</span>"; });
        html += "</div>";
      }
      body.innerHTML = html;
      if (!dialog.open) dialog.showModal();
      dialog.scrollTop = 0;
      history.replaceState(null, "", "#" + slug);
    }

    function syncFromHash() {
      var slug = decodeURIComponent(location.hash.replace(/^#/, ""));
      if (!slug) return;
      if (findTalk(slug)) openTalk(slug);
    }

    /* =====================================================================
       INIT + language switching
       ===================================================================== */
    function renderPage() {
      teardown();
      if (page.layout === "hub") renderHub();
      else renderDay();
    }

    renderPage();

    if (page.layout === "daypage") {
      var dialog = LDW.dialog();
      if (dialog) {
        dialog.addEventListener("close", function () {
          if (location.hash) history.replaceState(null, "", location.pathname + location.search);
        });
      }
      window.addEventListener("hashchange", syncFromHash);
      syncFromHash();
    }

    LDW.onLang(function () {
      renderPage();
      /* if the dialog is open, re-render its content in the new language */
      var dialog = LDW.dialog();
      if (dialog && dialog.open && location.hash) {
        var slug = decodeURIComponent(location.hash.replace(/^#/, ""));
        if (findTalk(slug)) openTalk(slug);
      }
    });
  });
})();
