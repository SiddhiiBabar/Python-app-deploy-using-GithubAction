html_content = """
<!DOCTYPE html>
<html>
<head>
  <title>Python App Deployment</title>
</head>
<body>
  <h1>🚀 Python App Successfully Deployed using GitHub Actions!</h1>
  <p>CI/CD Pipeline working perfectly.</p>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html generated successfully")
