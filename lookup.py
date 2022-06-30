import pathlib
import requests
import json
import argparse

def getApiKey(path):
    keyFile = pathlib.Path(path).expanduser()
    fileHandler = open(keyFile, 'r')
    apiKey = fileHandler.readline().strip()

    return apiKey

def buildUrl(word, apiKey):
    url = ('https://www.dictionaryapi.com/api/v3/references/collegiate/json/' +
            word + '?key=' + apiKey)
    return url

def fetchDefinitions(url):
    response = requests.get(url)
    result = json.loads(response.text)[0]

    return result['shortdef']

def printDefinitions(definitions):
    for i, definition in enumerate(definitions, 1):
        print(str(i) + '. ' + definition)

if __name__ == '__main__':
    path = '~/.api-keys/merriam-webster-dictionary.txt'

    description = 'Get the Merriam-Webster definition of a word'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('word', nargs=1, type=str, help="Word to be looked up.")
    args = parser.parse_args()

    url = buildUrl(args.word[0], getApiKey(path))
    defs = fetchDefinitions(url)

    printDefinitions(defs)

