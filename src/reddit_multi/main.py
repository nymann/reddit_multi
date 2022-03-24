from pathlib import Path
from typing import Optional

import praw
from praw.models import Subreddit
import typer

app = typer.Typer()


@app.command()
def main(
    subreddits: list[str],
    title: str = typer.Option(...),
    client_id: str = typer.Option(..., envvar="REDDIT_CLIENT_ID"),
    client_secret: str = typer.Option(..., envvar="REDDIT_CLIENT_SECRET"),
    refresh_token: str = typer.Option(..., envvar="REDDIT_REFRESH_TOKEN"),
    text: Optional[str] = typer.Option(None),
    image_path: Optional[Path] = typer.Option(None),
):
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent="Linux:reddit_multi:0.0.1 (by u/Overseer12)",
        refresh_token=refresh_token,
    )
    for subreddit_str in subreddits:
        subreddit: Subreddit = reddit.subreddit(subreddit_str)
        if image_path:
            subreddit.submit_image(title=title, image_path=str(image_path))
        else:
            subreddit.submit(title=title, selftext=text)


if __name__ == "__main__":
    app()
