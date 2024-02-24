# text request

## Curl

```sh
curl \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Write a story about a magic backpack"}]}]}' \
  -X POST https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_API_KEY
```

## Docs

* <https://ai.google.dev/tutorials/python_quickstart>
* <https://github.com/google/generative-ai-docs/blob/main/site/en/tutorials/python_quickstart.ipynb>
