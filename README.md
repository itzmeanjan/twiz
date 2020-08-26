# twiz
Your Twitter Account Data Analysis &amp; Visualization Tool &lt;3

## motivation

Being a data hunter ( yeah, you read it correct ), I love to collect available data & analyze it for finding hidden patterns in it.

That's why I downloaded my Twitter account data & started analyzing it. This tool can be used for analyzing your twitter account data without sending any of it to remote machines.

I'm adding some features here, if you feel some improvements can be done there, please feel free to contact me or you can always raise a PR.

## usage

**twiz** can be downloaded from PyPI. Make sure you've python _( >=3.7 )_ installed.

```bash
python3 -m pip install twiz
```

If you've added default _pip_ installation path to system **PATH** variable, then it can be invoked as below.

```
twiz path-to-twitter-data.zip sink/
```

## features

- Follwers & Followings
    - [x] [Twitter Followers And Followings Per Cent](./docs/twitterFollowersAndFollowingsForYOU.md)
    - [x] [Twitter Followers & Followers whom you're following vs Twitter Followings & Followings who're following you](./docs/twitterFollowersFollowingsAndIntersectionForYOU.md)

- Likes
    - [x] [Top 10 Twitter **#HASHTAGS** found in tweets liked by YOU](./docs/top10TwitterHashTagsFoundInTweetsLikedByYOU.md)

**This section will keep getting populated ;)**
