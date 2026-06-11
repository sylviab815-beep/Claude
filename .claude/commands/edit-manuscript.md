---
description: Run the editing pipeline on a manuscript with Track Changes
argument-hint: [manuscript-file]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, AskUserQuestion
---

Run the Manuscript Editor Pro editing pipeline on the manuscript at @$1.

Load the manuscript-editing skill and follow its complete workflow:

1. Ask the user which passes they want to run (full pipeline, line edit + proofread, individual passes, or custom)
2. Build a Voice Profile from the manuscript before editing
3. Run selected passes — every prose change delivered as Track Changes in the .docx
4. Generate the Editorial Report (.docx)
5. Produce the edited manuscript with Track Changes (.docx)

All changes appear as tracked revisions the author can accept or reject in Word/Google Docs.

Save all deliverables to the user's workspace folder.
