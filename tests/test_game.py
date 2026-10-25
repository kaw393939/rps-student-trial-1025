"""RPS-001 outcomes copied explicitly from SPEC.md."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_expected_outcome(player, computer, expected):
    assert determine_winner(player, computer) == expected


def test_submitted_round_uses_real_rules(monkeypatch):
    monkeypatch.setattr(web.random, "choice", lambda moves: "scissors")
    monkeypatch.setitem(web.app.config, "TESTING", True)

    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})

    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert '<p class="choice-label">You chose</p><p class="choice-value">Rock ' in page
    assert '<p class="choice-label">Computer chose</p><p class="choice-value">Scissors ' in page
    assert '<h2 id="game-heading">You win!</h2>' in page
    assert 'data-outcome="win"' in page
    assert "game rules not built yet" not in page
