import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="WebsiteExample")
@app.route(route="")  # Root route ("/")
def serve_website(req: func.HttpRequest) -> func.HttpResponse:
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Azure Function Website</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                text-align: center; 
                background-color: #f4f4f4;
            }
            .container { 
                margin-top: 50px;
            }
            img {
                width: 300px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Azure Function Website!</h1>
            <p>This website is served from an Azure Function.</p>
            <img src="https://source.unsplash.com/featured/?nature,water" alt="Random Nature Image">
        </div>
    </body>
    </html>
    """
    return func.HttpResponse(html_content, mimetype="text/html")
