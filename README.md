# gptty
Chat GPT wrapper in your TTY


## Configuration

`gptty` reads configuration settings from a file named gptty.ini located in the same directory as the main script. The file uses the INI file format, which consists of sections, each with its own key-value pairs.

| Month    | Savings | Month    | Savings |
| -------- | ------- | -------- | ------- |
| api_key  | String    | ""  |   The API key for OpenAI's GPT service  |
| gpt_version | String     | "3" |    The version of GPT to use  |
| your_name    | String    | "question"    |   The name of the input prompt  |
| gpt_name  | String    | "response"  |   The name of the generated response  |
| output_file | String     | "output.txt" |    The name of the file where the output will be saved  |
| model    | String    | "text-davinci-003"    |   The name of the GPT model to use  |
| temperature  | Float    | 0.0  |   The temperature to use for sampling  |
| max_tokens | Integer     | 250 |    The maximum number of tokens to generate for the response  |
| max_context_length    | Integer    | 5000    |   The maximum length of the input context  |


You can modify the settings in the configuration file to suit your needs. If a key is not present in the configuration file, the default value will be used. The [main] section is used to specify the program's settings. 

```ini
[main]
api_key=my_api_key
```


