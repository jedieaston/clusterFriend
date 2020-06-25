# Why?

Well, I needed a little thing to play with when messing with things like k8s or fly.io, so this is a flask app that returns
the:

+ external IP of the box
+ the hostname of where it is
+ the current time
+ a fortune from the Alpine (openBSD) fortune package.

It's fun and easy to see what exact container I just made a request to. Okay? Is that okay?

# No, it isn't.

Fine. clusterFriend is:
+ web scale (don't need to worry about keeping storage anywhere!)
+ https ready*
+ enterprise ready (gives fortunes in just megabytes of RAM! 50ms response time)
+ serverless

That's better. Linkedin is in the profile! /s

# How do I use it?

Just do docker build . (or if you aren't somewhere with docker, pip install -r requirements.txt && cd clusterFriend && gunicorn -p 8080 app:app)


\* you know, with nginx. I was keeping it simple, most k8s work I've done I use separate proxy stuff. and fly does it for you.
