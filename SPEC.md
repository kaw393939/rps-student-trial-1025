# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

Implement determine_winner(player, computer) for one independent round, returning win, lose, or tie from the player’s perspective. Follow the nine expected results above and keep the supplied interface and server. Show both choices and the correct result; choosing again starts a fresh round. Add nine explicit rule tests and a real submitted-round test with a fixed computer move. Run .venv/bin/python -m pytest, review the diff against this spec, then check the browser and record actual observations. No score, saved history, or additional features.

### Checks

AI runs nine explicit rule cases plus a complete submitted round with a fixed computer move, then reviews the diff against this spec. The student plays, inspects a rule and its test, and gives feedback. Passing rule tests alone does not establish that the browser is usable or every control is wired correctly.

### Work record

- Issue: https://github.com/kaw393939/rps-student-trial-1025/issues/1
- Implementation: [game.py](game.py) implements one independent round from the player's perspective, keeping the supplied interface and server.
- Checks: `.venv/bin/python -m pytest` passed all 22 tests: nine explicit matchups and one real Flask POST/result check with fixed computer scissors in [tests/test_game.py](tests/test_game.py), plus 12 supplied shell tests. Reviewed the diff against RPS-001: no score, history, or additional features.
- Student checks: reported pytest result of 22 passed. Browser observations (player/computer): Paper/Paper tie, Rock/Rock tie, Scissors/Paper “You win!”, and Rock/Scissors “You win!”. Both choices were visible; each choice started a new round; the unfinished notice was gone. Tab focused Rock and Enter played a correct round. These observations cover four browser matchups, not all nine.
