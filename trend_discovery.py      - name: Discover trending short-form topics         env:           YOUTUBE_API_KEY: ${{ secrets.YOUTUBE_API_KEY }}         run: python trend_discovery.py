      - name: Discover trending short-form topics
        env:
          YOUTUBE_API_KEY: ${{ secrets.YOUTUBE_API_KEY }}
        run: python trend_discovery.py
