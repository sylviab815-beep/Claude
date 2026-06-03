# Installation Guide

## Claude.ai

1. Upload the ZIP as a custom Skill.
2. Enable the Skill.
3. Start with: `Use the Full-Stack Manuscript Polish Skill. Run Pass 1.`

## Claude Code / Codex-style local use

Place the `full-stack-manuscript-polish` folder inside the workspace and tell the model:

`Use the skill in full-stack-manuscript-polish/SKILL.md for this manuscript.`

## ChatGPT Projects / Custom GPTs

If your platform does not support Claude-style Skills, upload `SKILL.md` and the files in `/resources` as project knowledge or GPT knowledge. Then paste this into the project instructions:

`Use the uploaded Full-Stack Manuscript Polish Skill as the editorial operating system. Run one pass at a time. Do not rewrite by default. Use the templates and framework resources when producing output.`
