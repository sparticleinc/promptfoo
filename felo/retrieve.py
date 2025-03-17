import json


json_path = "C:/Users/YiYang/Downloads/358549f7-03cd-4a42-a12d-e58bb90f9b66.json"

# Load the JSON file
datas = []
with open(json_path, 'r', encoding="utf-8") as fp:
    data = json.load(fp)
    datas.extend(data.get("datas"))

def call_api(query, options, context):
    # find data by query
    data = None
    for d in datas:
        if d.get("question") == query:
            data = d
            break
    if not data:
        return {"error": f"Data not found"}
    
    result = {
        "output": data.get("answer"),
    }

    # Include error handling and token usage reporting as needed
    # if some_error_condition:
    #     result['error'] = "An error occurred during processing"
    #
    # if token_usage_calculated:
    #     result['tokenUsage'] = {"total": token_count, "prompt": prompt_token_count, "completion": completion_token_count}

    return result