import json

def lambda_handler(event, context):
    # Cricket match dataset
    cricket_data = {
        "match": "India vs Afghanistan",
        "status": "In Progress",
        "score": "184/2",
        "overs": "44.4",
        "batting_team": "India",
        "run_rate": "4.14"
    }

    # API Gateway response format with CORS headers enabled
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(cricket_data)
    }