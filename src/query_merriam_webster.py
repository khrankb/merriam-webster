import json
import argparse
import logging
import requests


def get_word_definition(word):
    api_key = "f0fea427-4584-4210-83d5-baecc9aeb6fe"
    api_url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{0}?key={1}".format(word, api_key)
    api_response = requests.get(api_url)
    api_response.encoding = 'utf-8'
    if api_response.status_code == 200:
        logging.info("Connection Successful.")
        return json.loads(api_response.content)
    else:
        logging.info("Connection Failed.")


def fetch_result(word):
    res_json = get_word_definition(word)
    if res_json:
        print("Word Found")
        word_pronunciation = res_json[0]["hwi"]["prs"][0]["mw"]
        word_class = res_json[0]['fl']
        short_def = res_json[0]["shortdef"][0]
        result = "{} ({}): {}".format(word_pronunciation, word_class, short_def)
        return result
    else:
        print("Error: The word you've entered isn't in the dictionary.")

def main():
    arg_parser = argparse.ArgumentParser(
        description="CLI utility to query the merriam-webster dictionary"
    )
    arg_parser.add_argument("-w", "--word", type=str, help="Enter a word to find definition")
    args = arg_parser.parse_args()
    output = fetch_result(args.word)
    print(output)


if __name__ == "__main__":
    main()
