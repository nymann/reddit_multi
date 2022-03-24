## Reddit Multi

Create a new text or image submission to Reddit from your command line to one or more subreddits at once.

### Installation

```sh
python -m pip install git+https://github.com/nymann/reddit_multi.git
```

### Examples

```sh
reddit_multi --title "Testing image upload" --client-id REDDIT_CLIENT_ID --client-secret REDDIT_CLIENT_SECRET --refresh-token REFRESH_TOKEN --image-path /tmp/test.jpg testingground4bots bottesting
```

The above command will upload the image located at the path `/tmp/test.jpg` to the two subreddits `r/testingground4bots` and `r/bottesting`. A guide to setting up the `client-id`, `client-secret` and `refresh-token` can be found [here](https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/).

Alternative the `client-id`, `client-secret` and `refresh-token` can be read from the environment variables, like so:

```sh
export REDDIT_CLIENT_SECRET=blabla
export REDDIT_CLIENT_ID=blabla
export REFRESH_TOKEN=blabla

reddit_multi --title "Testing image upload" --image-path /tmp/test.jpg testingground4bots bottesting
```
