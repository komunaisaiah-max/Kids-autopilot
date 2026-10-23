.github/workflows/autopilot.yml
name: Kids Channel Autopilot

on:
  schedule:
    - cron: "0 22 * * *"
  workflow_dispatch: {}

permissions:
  contents: write

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install requests google-api-python-client google-auth
      - name: Run autopilot
        env:
          YOUTUBE_API_KEY: ${{ secrets.YOUTUBE_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          YT_CLIENT_ID: ${{ secrets.YT_CLIENT_ID }}
          YT_CLIENT_SECRET: ${{ secrets.YT_CLIENT_SECRET }}
          YT_REFRESH_TOKEN: ${{ secrets.YT_REFRESH_TOKEN }}
        run: python autopilot.py
      - name: Save results
        run: |
          git config user.name "autopilot"
          git config user.email "autopilot@users.noreply.github.com"
          git add -A
          git diff --cached --quiet || git commit -m "Autopilot $(date -u +%F)"
          git push
