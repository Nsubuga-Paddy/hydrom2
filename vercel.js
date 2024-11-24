{
    "builds": [{
        "src": "hydromapp/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
    }],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "hydromapp/wsgi.py"
        }
    ]
}
