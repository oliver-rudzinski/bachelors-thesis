def enrich_weather(dicts):
    for name, content in dicts.items():
        url = "http://api.weatherapi.com/v1/history.json"
        api_key = # omitted
        res = get(
            url,
            params={
                "key": api_key,
                "q": "48.781318, 9.180211",
                "dt": content["BusinessDayDate"],
            },
        )

        data = json.loads(res.text)["forecast"]["forecastday"][0]["day"][
            "avgtemp_c"
        ]

        content["temp"] = data