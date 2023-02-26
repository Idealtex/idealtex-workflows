# Hello world docker action

This action prints "Hello World" or "Hello" + the name of a person to greet to the log.

## Inputs

## `NEW_VERSION`

The name of the person to greet. Default `"World"`.

## `SERVICE_NAME`

**Required** The name of the person to greet. Default `"World"`.

## Example usage

uses: actions/hello-world-docker-action@v2
with:
  who-to-greet: 'Mona the Octocat'