.github/workflows/autopilot.yml
name: Kids Channel Autopilot

on:
  workflow_dispatch:
  schedule:
    - cron: "0 22 * * *"

permissions:
  contents: write

jobs:
  create-content-brief:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Generate content brief
        run: python autopilot.py

      - name: Save report
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add reports/
          if ! git diff --cached --quiet; then
            git commit -m "Generate kids content brief"
            git push
          fi
          
from datetime import datetime, timezone
from pathlib import Path

IDEAS = [
    {
        "title": "The Little Turtle Who Never Gave Up",
        "hook": "Everyone reached the hill first, but the little turtle kept going.",
        "lesson": "Patience and steady effort matter.",
        "scenes": [
            "Meet the determined little turtle.",
            "The turtle faces a small obstacle.",
            "A friend offers encouragement.",
            "The turtle keeps trying and reaches the goal.",
            "Celebrate persistence and kindness."
        ]
    },
    {
        "title": "The Bird Who Shared Her Umbrella",
        "hook": "A sudden rainstorm caught three forest friends far from home.",
        "lesson": "Kindness grows when we share.",
        "scenes": [
            "Introduce the bird and her umbrella.",
            "Friends get caught in the rain.",
            "The bird makes room for everyone.",
            "They travel together to shelter.",
            "End with a message about sharing."
        ]
    },
    {
        "title": "The Tiny Seed's Big Dream",
        "hook": "A tiny seed dreamed of becoming a mighty tree.",
        "lesson": "Small beginnings can lead to wonderful things.",
        "scenes": [
            "Show the tiny seed in the soil.",
            "Rain and sunlight arrive.",
            "The seed waits through a difficult day.",
            "A green sprout appears and grows.",
            "Celebrate patience and caring for nature."
        ]
    },
    {
        "title": "Milo Learns to Tell the Truth",
        "hook": "Milo made a mistake and had to decide what to do next.",
        "lesson": "Honesty helps people trust one another.",
        "scenes": [
            "Introduce Milo and his friends.",
            "A small mistake happens.",
            "Milo feels worried.",
            "Milo tells the truth and helps fix it.",
            "End with an encouraging lesson."
        ]
    },
    {
        "title": "The Friends Who Built a Bridge",
        "hook": "A little stream separated two groups of forest friends.",
        "lesson": "Teamwork helps solve problems.",
        "scenes": [
            "Show the stream and the problem.",
            "Each friend suggests an idea.",
            "They plan a safe solution.",
            "They work together with adult guidance.",
            "Celebrate teamwork and friendship."
        ]
    }
]


def main():
    today = datetime.now(timezone.utc).date()
    idea = IDEAS[today.toordinal() % len(IDEAS)]

    report = [
        "# Kids Channel Content Brief",
        "",
        f"Generated: {today.isoformat()} UTC",
        "",
        "> Planning ideas only. This script does not research live trends,",
        "> create a finished video, or upload or publish content.",
        "",
        f"## {idea['title']}",
        "",
        f"**Opening hook:** {idea['hook']}",
        "",
        f"**Positive lesson:** {idea['lesson']}",
        "",
        "### Five-scene outline",
        ""
    ]

    for number, scene in enumerate(idea["scenes"], start=1):
        report.append(f"{number}. {scene}")

    report.extend([
        "",
        "### Production checklist",
        "",
        "- Write original narration for the selected story.",
        "- Review the script for age suitability.",
        "- Use visuals and music you have permission to use.",
        "- Check captions, audio, and thumbnail before publishing.",
        "- Review the finished video manually.",
        "- Do not publish until the channel owner approves it.",
        ""
    ])

    folder = Path("reports")
    folder.mkdir(exist_ok=True)
    output = folder / f"content-brief-{today.isoformat()}.md"
    output.write_text("\n".join(report), encoding="utf-8")
    print(f"SUCCESS: Created {output}")


if __name__ == "__main__":
    main()
    
