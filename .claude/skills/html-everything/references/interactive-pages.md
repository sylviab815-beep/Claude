# Interactive Pages

Quizzes, calculators, "which character are you" widgets, simple games, promo widgets, choose-your-own-adventure mini-experiences.

## When to use

- "Make me a 'which character are you' quiz"
- "Build a calculator for [thing]"
- "Promo widget for [book]"
- "Choose-your-own-adventure based on [chapter]"
- "Family tree clicker"
- "Audio sample player"

## Constraints

- **Single file, no build process.** Plain HTML/CSS/JS.
- **No external dependencies.** No React, no jQuery, no frameworks. Vanilla JS only.
- **Mobile-first.** Most interactive promo gets shared on phones.
- **No localStorage / sessionStorage** unless the user explicitly says it's okay — Claude.ai artifacts can't use them, and many embeds block them.
- **Light mode default.** Add `:root { color-scheme: light; }`.
- **Keep state in memory.** Use plain JS variables / `let state = {...}`. State resets on reload — that's fine.

## Pattern 1: "Which character are you" quiz

The most common promo widget. 5-8 questions, each with 3-4 answers. Each answer adds points to a character. Highest score = result.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Which [Book] Character Are You?</title>
<style>
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 0;
  font-family: Georgia, 'Iowan Old Style', serif;
  background: #faf8f4;
  color: #1a1a1a;
  line-height: 1.5;
}
.page { max-width: 600px; margin: 0 auto; padding: 32px 24px; }
h1 { text-align: center; font-size: 28px; margin: 0 0 32px; }
.question {
  background: #fff;
  border: 1px solid #e4dfd5;
  padding: 24px;
  margin-bottom: 16px;
}
.question h2 { font-size: 18px; margin: 0 0 16px; }
.answers { display: flex; flex-direction: column; gap: 8px; }
.answer {
  display: block;
  padding: 12px 16px;
  background: #faf8f4;
  border: 1px solid #d4cfc5;
  cursor: pointer;
  font-family: inherit;
  font-size: 15px;
  text-align: left;
  transition: background 0.15s, border-color 0.15s;
}
.answer:hover { background: #f0e8d4; }
.answer.selected { background: #5a2a2a; color: #faf8f4; border-color: #5a2a2a; }
.submit {
  display: block;
  width: 100%;
  padding: 16px;
  background: #1a1a1a;
  color: #faf8f4;
  border: 0;
  font-family: inherit;
  font-size: 16px;
  letter-spacing: 0.08em;
  cursor: pointer;
  margin-top: 24px;
}
.submit:disabled { background: #888; cursor: not-allowed; }
.result { display: none; text-align: center; padding: 32px 0; }
.result.show { display: block; }
.result h2 { font-size: 32px; margin: 0 0 16px; }
.result .description {
  font-size: 17px;
  line-height: 1.7;
  max-width: 480px;
  margin: 0 auto 24px;
}
.result .retake {
  font-family: inherit;
  background: none;
  border: 1px solid #1a1a1a;
  padding: 12px 24px;
  font-size: 14px;
  letter-spacing: 0.06em;
  cursor: pointer;
}
@media (max-width: 480px) {
  h1 { font-size: 22px; }
  .question { padding: 16px; }
}
</style>
</head>
<body>
<div class="page">

<h1>Which [Book] Character Are You?</h1>

<div id="quiz"></div>

<button id="submitBtn" class="submit" disabled>See your result</button>

<div id="result" class="result">
  <h2 id="resultName"></h2>
  <p class="description" id="resultDesc"></p>
  <button class="retake" onclick="location.reload()">Take it again</button>
</div>

</div>

<script>
const questions = [
  {
    q: "It's pre-dawn. The cottage is cold. What do you do first?",
    answers: [
      { text: "Get up and check the chapel through the window.", chars: { else: 2 } },
      { text: "Stay in bed and listen.", chars: { callum: 2 } },
      { text: "Light the fire. Make tea.", chars: { agnes: 2 } },
      { text: "Walk the perimeter.", chars: { margery: 2 } },
    ]
  },
  // ... more questions
];

const characters = {
  else: {
    name: "Else",
    desc: "You're the one who walks into the dark first because someone has to. Direct, dry, body-anchored. You carry what no one else will."
  },
  callum: {
    name: "Callum",
    desc: "You read everything — texts, faces, silences. You'd rather be wrong from study than right by accident."
  },
  agnes: {
    name: "Agnes",
    desc: "You're the one who waits. You've been ready for two months. You know when to speak and when not to."
  },
  margery: {
    name: "Margery",
    desc: "You're the knife at the elbow. Loyal, foul-mouthed, useless for small talk, essential at thresholds."
  },
};

const state = {
  answers: new Array(questions.length).fill(null),
};

function renderQuiz() {
  const quiz = document.getElementById('quiz');
  quiz.innerHTML = questions.map((q, qi) => `
    <div class="question">
      <h2>${qi + 1}. ${q.q}</h2>
      <div class="answers">
        ${q.answers.map((a, ai) => `
          <button class="answer" data-q="${qi}" data-a="${ai}">${a.text}</button>
        `).join('')}
      </div>
    </div>
  `).join('');
  quiz.querySelectorAll('.answer').forEach(btn => {
    btn.addEventListener('click', e => {
      const qi = +e.target.dataset.q;
      const ai = +e.target.dataset.a;
      state.answers[qi] = ai;
      // visual: clear other answers in this question
      e.target.parentElement.querySelectorAll('.answer').forEach(b => b.classList.remove('selected'));
      e.target.classList.add('selected');
      // enable submit if all answered
      document.getElementById('submitBtn').disabled = state.answers.some(a => a === null);
    });
  });
}

document.getElementById('submitBtn').addEventListener('click', () => {
  // tally
  const scores = {};
  state.answers.forEach((ai, qi) => {
    const charsForAnswer = questions[qi].answers[ai].chars;
    for (const c in charsForAnswer) {
      scores[c] = (scores[c] || 0) + charsForAnswer[c];
    }
  });
  // pick highest
  const winner = Object.entries(scores).sort((a, b) => b[1] - a[1])[0][0];
  const char = characters[winner];
  // show result
  document.getElementById('resultName').textContent = char.name;
  document.getElementById('resultDesc').textContent = char.desc;
  document.getElementById('quiz').style.display = 'none';
  document.getElementById('submitBtn').style.display = 'none';
  document.getElementById('result').classList.add('show');
});

renderQuiz();
</script>

</body>
</html>
```

## Pattern 2: Choose-your-own scene

A branching mini-story. Each "page" is a scene; choices lead to other scenes. State is just the current scene ID.

```javascript
const scenes = {
  start: {
    text: "You're at the threshold of the chapel. The wind is bitter. You can:",
    choices: [
      { text: "Cross the threshold.", goto: "inside" },
      { text: "Wait for someone else.", goto: "wait" },
    ]
  },
  inside: { text: "...", choices: [...] },
  wait: { text: "...", choices: [...] },
  // ...
};

let current = "start";
function render() {
  const s = scenes[current];
  document.getElementById('text').textContent = s.text;
  document.getElementById('choices').innerHTML = s.choices.map(c =>
    `<button onclick="current='${c.goto}'; render();">${c.text}</button>`
  ).join('');
}
render();
```

## Pattern 3: Audio sample player

For audiobook promo. Single audio file + a play button + a transcript below.

```html
<audio id="player" preload="metadata" src="[AUDIO_URL]"></audio>
<button id="playBtn">▶ Play</button>
<div id="transcript">[Transcript text]</div>

<script>
const player = document.getElementById('player');
const btn = document.getElementById('playBtn');
btn.addEventListener('click', () => {
  if (player.paused) {
    player.play();
    btn.textContent = '⏸ Pause';
  } else {
    player.pause();
    btn.textContent = '▶ Play';
  }
});
player.addEventListener('ended', () => { btn.textContent = '▶ Play again'; });
</script>
```

Audio files in promo HTML: best hosted on a CDN or pasted as a `<source>` with a hosted URL. Self-contained audio via `data:` URL works but balloons file size.

## Pattern 4: Family tree / character map

Static SVG works best. Pan/zoom isn't necessary for most author use cases — keep it simple.

```html
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto;">
  <!-- nodes -->
  <g class="node" transform="translate(400, 100)">
    <rect x="-80" y="-30" width="160" height="60" fill="#faf8f4" stroke="#1a1a1a"/>
    <text text-anchor="middle" y="5" font-family="Georgia, serif" font-size="14">Character Name</text>
  </g>
  <!-- lines -->
  <line x1="400" y1="130" x2="200" y2="200" stroke="#888"/>
  <!-- ... -->
</svg>
```

Add click handlers if the user wants nodes to open detail panels.

## Pattern 5: Countdown timer (release day)

```html
<div id="countdown" style="text-align: center; font-family: Georgia, serif;">
  <div id="days">--</div>
  <div>days until [BOOK TITLE] releases</div>
</div>

<script>
const releaseDate = new Date('YYYY-MM-DDT00:00:00');
function update() {
  const now = new Date();
  const days = Math.max(0, Math.ceil((releaseDate - now) / (1000 * 60 * 60 * 24)));
  document.getElementById('days').textContent = days;
}
update();
setInterval(update, 1000 * 60 * 60); // re-check every hour
</script>
```

## What NOT to build

- Anything that needs a server (login, real user accounts, persistent data)
- Anything that needs a database
- Anything with payment processing
- Anything that scrapes external sites

If the user asks for one of these, redirect them to the right tool (ConvertKit for email capture, Shopify/Gumroad for sales, etc.) instead of trying to fake it in HTML.
