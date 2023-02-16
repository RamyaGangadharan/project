from flask import Flask,request,render_template

app = Flask(__name__)

test= """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1">
  	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
  	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
	<title>Terraform Project</title>
</head>
<body>
	<div class="container my-5">
		<div class="bg-image p-5 text-center shadow-1-strong rounded mb-5 text-white" style="background-image: url('https://images.hdqwalls.com/download/joining-lines-5k-kl-1920x1080.jpg');">
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<h1 class="mb-1 h1">Flask Application with Nginx</h1>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
			<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;">&nbsp;</p>
		</div>
</div>
</body>
"""
@app.route('/')
def webpage1():
	try:
		return test
	except Exception as e:
		return "Error in code"

if __name__ == "__main__":
	app.run(port=5000)
